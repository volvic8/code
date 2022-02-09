# https://note.nkmk.me/python-pandas-read-excel/

import pandas as pd
import os 

print(os.getcwd())

df = pd.read_excel(r"C:\work\data\sample.xlsx", sheet_name=0, index_col=0)
print(df)

# 行, 列
print(df.iat[0, 1])