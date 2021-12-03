#! /usr/bin/env python3

import os
import sys
import openpyxl

xls_exts = (".xls", ".xlsx", ".xlsm", ".xlsb", ".xlt", ".xltx", ".xltm", ".xla", ".xlam")

print(len(sys.argv))
if len(sys.argv) > 1:
    parent_path = sys.argv[1]
else:
    parent_path = os.getcwd()

for folder_path, sub_folder, sub_file in os.walk(parent_path):
    for file in sub_file:
        ext = os.path.splitext(file)[1].lower()
        if ext not in xls_exts:
            continue

        path = folder_path + "\\" + file
        print(file)
        book = openpyxl.load_workbook(path)
        sheets = book.sheetnames
        for sheet in sheets:
            if book[sheet].sheet_state != "hidden":
                print(sheet)
