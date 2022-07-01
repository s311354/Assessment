import argparse
import threading
import logging
import pandas as pd

from typing import List
from testplan import TestPlan
from collections import defaultdict


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()

    parser.add_argument(
        'outputformats',
        metavar='outputformats',
        type=str,
        nargs='+',
        help='If a single file format is passed in, then we assume it contains a '
        'semicolon-separated list of files that we expect this script to '
        'output. If multiple file formats are passed in, then we assume output file formats '
        'are listed directly as arguments. (Temporarily only support one xlsx formats)')
    parser.add_argument(
        'serialnumberlist',
        metavar='serialnumberlist',
        type=str,
        nargs='+',
        help='If a single serial number is passed in, then we assume it contains a '
        'semicolon-separated list of serial numbers that we expect this script to '
        'output. If multiple serial numbers are passed in, then we assume serial numbers '
        'are listed directly as arguments.')
    parser.add_argument(
        '--browser_type',
        default='Chrome',
        type=str,
        choices=['Chrome', 'Safari', 'Firefox'],
        help='The owner you want to choose the browser on a remote machine.')
    parser.add_argument(
        '--url',
        default='https://www.barco.com/en/clickshare/support/warranty-info',
        type=str,
        help='The owner you want to choose the url to create the test plan and test cases.')
    parser.add_argument(
        '--tolerance',
        default=6,
        type=int,
        help='The owner you could set tolerance to the network latancy.')
    parser.add_argument(
        '--output_file_name',
        default='warranty_defect',
        type=str,
        choices=['warranty_defect'],
        help='The owner you want to choose output file name.')

    return parser


def dumpspreadsheet(output, df_data):
    # Declare xlsx Sheet Name
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df_data.to_excel(writer,
                         sheet_name='Defect',
                         header=True, index=True)


def testscope(url: str, browser_type: str, serialnumbers: List[str], tolerance: int, output_file: str) -> None:
    testplan = TestPlan(url, browser_type)

    threads = []
    results = defaultdict(str)

    for serialnumber in serialnumbers:
        logging.info('Starting the test plan thread')
        thread = threading.Thread(name='blocking',
                                  target=testplan.createtestcases,
                                  args=(serialnumber, tolerance, results))
        threads.append(thread)
        thread.daemon = True
        # start the threads
        thread.start()

    for thread in threads:
        # wait for the threads to complete
        thread.join()

    # create the defect report

    df_warranyinfo = pd.DataFrame([[hmap[0], hmap[1]] for hmap in results.items()])
    df_warranyinfo.columns = ['SerialNumber', 'Warranty results']
    dumpspreadsheet('testcases/' + output_file, df_warranyinfo)


if __name__ == '__main__':
    parser = create_parser()
    args = parser.parse_args()

    if len(args.serialnumberlist) == 1:
        # If we only get a single argument, then it must be a file containing
        # list of outputs.
        with open(args.serialnumberlist[0]) as serialnumberlist:
            serialnumbers = [line.strip() for line in serialnumberlist.read().split(';')]
    else:
        serialnumbers = args.serialnumberlist

    if len(args.outputformats) == 1:
        # If we only get a single argument, then it must be a file containing
        # list of outputs.
        with open(args.outputformats[0]) as output_list_file:
            outputformats = [line.strip() for line in output_list_file.read().split(';')]
    else:
        outputformats = args.outputformats

    output_file = args.output_file_name + '.' + outputformats[1]

    testscope(url=args.url, browser_type=args.browser_type, serialnumbers=serialnumbers, tolerance=args.tolerance, output_file=output_file)
