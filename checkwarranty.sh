#!/bin/sh
#
:$ python3 checkclicksharewarranty.py --browser_type Chrome --tolerance 8 serialnumberlist
:usage: checkclicksharewarranty.py [-h]
:                                  [--browser_type {Chrome,Safari,Firefox}]
:                                  [--url URL] [--tolerance TOLERANCE]
:                                  [--output_file_name {warranty_defect}]
:                                  outputformats [outputformats ...]
:                                  serialnumberlist [serialnumberlist ...]
#

python3 checkclicksharewarranty.py --browser_type Chrome \
                                    --tolerance 8 \
                                    outputformats serialnumberlist
