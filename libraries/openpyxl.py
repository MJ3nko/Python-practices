from openpyxl import Workbook
from openpyxl.chart import BarChart, Reference

workbook = Workbook()
worksheet = workbook.active

data = [
    ["Fruit", "Quantity"],
    ["Kiwi", 3],
    ["Grape", 15],
    ["Apple", 3],
    ["Peach", 3],
    ["Pomegranate", 3],
    ["Pear", 3],
    ["Tangerine", 3],
    ["Blueberry", 3],
    ["Mango", 3],
    ["Watermelon", 3],
    ["Blackberry", 3],
    ["Orange", 3],
    ["Raspberry", 3],
    ["Banana", 3]
]

worksheet.freeze_panes = "A2"

for row in data:
    worksheet.append(row)

"""
# Insert a column before the existing column 1 ("A")
sheet.insert_cols(idx=1)

# Insert 5 columns between column 2 ("B") and 3 ("C")
sheet.insert_cols(idx=3, amount=5)


# Delete the created columns
sheet.delete_cols(idx=3, amount=5)
sheet.delete_cols(idx=1)

# Insert a new row in the beginning
sheet.insert_rows(idx=1)

# Insert 3 new rows in the beginning
sheet.insert_rows(idx=1, amount=3)

# Delete the first 4 rows
sheet.delete_rows(idx=1, amount=4)
print_rows()

"""
worksheet.auto_filter.ref = worksheet.dimensions  # Add filter to all cells
worksheet.auto_filter.add_sort_condition("A1")

chart = BarChart()
data = Reference(worksheet=worksheet,
                 min_row=1,
                 max_row=int(worksheet.max_row),
                 min_col=2,
                 max_col=2)

chart.add_data(data, titles_from_data=True)
worksheet.add_chart(chart, "E2")
print(worksheet['A1'].value)


print("In the previous line, the ws.dimensions contains all cells, that have data in it.")
workbook.save("Basic_excel.xlsx")
