import pandas as pd

data1 = {'Column1': [1, 2, 3, 4],
         'Column2': ['A', 'B', 'C', 'D']}
df1 = pd.DataFrame(data1)

data2 = {'Value': [10, 20, 30, 40],
         'Category': ['X', 'Y', 'Z', 'W']}
df2 = pd.DataFrame(data2)


with pd.ExcelWriter('pandas_worksheets.xlsx', engine='xlsxwriter') as writer:
    df1.to_excel(writer, sheet_name='Sheet1', index=False)
    df2.to_excel(writer, sheet_name='Sheet2', index=False)