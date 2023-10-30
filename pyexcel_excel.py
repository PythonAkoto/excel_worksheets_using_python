import pyexcel as pe

data1 = [['Column1', 'Column2'],
         [1, 'A'],
         [2, 'B'],
         [3, 'C'],
         [4, 'D']]

data2 = [['Value', 'Category'],
         [10, 'X'],
         [20, 'Y'],
         [30, 'Z'],
         [40, 'W']]

sheet1 = pe.Sheet(data1)
sheet2 = pe.Sheet(data2)

book = pe.Book({"Sheet1": sheet1, "Sheet2": sheet2})
book.save_as("pyexcel_worksheets.xlsx")
