#! /usr/bin/env python3

import os
import sys
import openpyxl

xls_exts = (".xls", ".xlsx", ".xlsm", ".xlsb",
            ".xlt", ".xltx", ".xltm", ".xla", ".xlam")

if len(sys.argv) > 1:
    parent_path = sys.argv[1]
else:
    # ディレクトリの指定がなければカレントディレクトリを設定
    parent_path = os.getcwd()

# 指定ディレクトリ配下のファイルを処理
for folder_path, sub_folder, sub_file in os.walk(parent_path):
    for file in sub_file:
        # excel以外のファイルはスキップ
        ext = os.path.splitext(file)[1].lower()
        if ext not in xls_exts:
            continue

        full_path = folder_path + "\\" + file
        print(file)
        book = openpyxl.load_workbook(full_path)
        sheets = book.sheetnames
        for sheet in sheets:
            # 非表示シートを除外
            if book[sheet].sheet_state != "hidden":
                print(sheet)
