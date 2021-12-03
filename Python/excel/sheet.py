import openpyxl

# ブックを取得
book = openpyxl.load_workbook("C:\\work\\data\\test_data\\シート.xlsx")
# シートを取得 
sheets = book.sheetnames

print(sheets)