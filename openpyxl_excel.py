from openpyxl import Workbook

# Create a new workbook
workbook = Workbook()

# Create the first worksheet
worksheet1 = workbook.active
worksheet1.title = "Sheet1"

# Add data to the first worksheet
data1 = {'Column1': [1, 2, 3, 4],
         'Column2': ['A', 'B', 'C', 'D']}

for row_data in data1.values():
    worksheet1.append(row_data)

# Create the second worksheet
worksheet2 = workbook.create_sheet(title="Sheet2")

# Add data to the second worksheet
data2 = {'Value': [10, 20, 30, 40],
         'Category': ['X', 'Y', 'Z', 'W']}

for row_data in data2.values():
    worksheet2.append(row_data)

# Save the workbook to a file
workbook.save("openpyxl_worksheets.xlsx")