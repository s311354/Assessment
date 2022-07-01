## Assessment for the Software Engineer In Test ##

### Introduction ###

This repository is useful as a interview assessment with Python 3.7+.

### Prerequisite Packages ###

The convenient and safy way to execute this test scope is by installing the dependencies. Please run the following command in the terminal.

```
$ pip install -r requirements.txt
```

### Quick Start

```
$ ./checkwarranty.sh
```

### Usages ###
```
$ python3 checkclicksharewarranty.py -h
usage: checkclicksharewarranty.py [-h]
                                  [--browser_type {Chrome,Safari,Firefox}]
                                  [--url URL] [--tolerance TOLERANCE]
                                  [--output_file_name {warranty_defect}]
                                  outputformats [outputformats ...]
                                  serialnumberlist [serialnumberlist ...]

positional arguments:
  outputformats         If a single file format is passed in, then we assume
                        it contains a semicolon-separated list of files that
                        we expect this script to output. If multiple file
                        formats are passed in, then we assume output file
                        formats are listed directly as arguments. (Temporarily
                        only support one xlsx formats)
  serialnumberlist      If a single serial number is passed in, then we assume
                        it contains a semicolon-separated list of serial numbers that
                        we expect this script to test. If multiple serial
                        numbers are passed in, then we assume serial numbers are
                        listed directly as arguments.

optional arguments:
  -h, --help            show this help message and exit
  --browser_type {Chrome,Safari,Firefox}
                        The owner you want to choose the browser on a remote
                        machine.
  --url URL             The owner you want to choose the url to create the
                        test plan and test cases.
  --tolerance TOLERANCE
                        The owner you could set tolerance to the network
                        latancy.
  --output_file_name {warranty_defect}
                        The owner you want to choose output file name.
```

### Files ###

```
.
├── README.md
├── __init__.py
├── __pycache__
│   ├── __init__.cpython-37.pyc
│   ├── test_sample1.cpython-37-pytest-7.1.2.pyc
│   └── testplan.cpython-37.pyc
├── checkclicksharewarranty.py
├── checkwarranty.sh
├── outputformats
├── requirements.txt
├── serialnumberlist
├── testcases
│   ├── __init__.py
│   └── warranty_defect.xlsx
└── testplan.py
```

### Defect References ###

To verify the valid serial number, please directly list the serial numbers and separate by semicolon in [`serialnumberlist`](serialnumberlist)

Please check the [`Warranty Report`](testcases/warranty_defect.xlsx) in [`testcases`](testcases/)
