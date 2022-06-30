from testplan import TestPlan
import argparse
import List
import threading

def create_parser() -> argparse.ArgumentParser:
    """Description

    :param param:  Description
    :type  param:  Type

    :return:  Description
    :rtype:  Type

    :raise e:  Description
    """
    parser = argparse.ArgumentParser()

    parser.add_argument(
        'serialnumberlist',
        metavar='serialnumberlist',
        type=str,
        nargs='+',
        help='If a single serial number is passed in, then we assume it contains a '
        'semicolon-separated list of files that we expect this script to '
        'output. If multiple serial numbers are passed in, then we assume stocks '
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

    return parser


def main(url: str, browser_type: str, serialnumbers: List[str]) -> None:
    testplan = TestPlan(url, browser_type)
    e = threading.Event()

    threads = []
    for serialnumber in serialnumbers:
        threads.append(threading.Thread(name='non-blocking',
                                        target=testplan.createtestcase,
                                        args=(e, serialnumber)))

    for thread in threads:
        thread.start()

    e.clear()


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

    main(url=args.url, browser_type=args.browser_type, serialnumbers=serialnumbers)
