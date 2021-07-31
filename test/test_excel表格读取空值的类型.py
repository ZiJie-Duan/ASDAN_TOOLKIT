import xlrd



tables_data = xlrd.open_workbook(r"C:\Users\Peter Duan\Desktop\test.xls")

table = tables_data.sheet_by_name("CITY")



line_data = table.row_values(3, start_colx=0, end_colx=None)

print(line_data)
input()