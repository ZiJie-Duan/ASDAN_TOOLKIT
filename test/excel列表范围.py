import xlrd

data = xlrd.open_workbook(r"C:\Users\lucyc\Desktop\test.xlsx")

table = data.sheets()[0]          #通过索引顺序获取

names = data.sheet_names()    #返回book中所有工作表的名字
print(names)

nrows = table.nrows  #获取该sheet中的有效行数
print(nrows)

a = table.row_values(0, start_colx=0, end_colx=None)   #返回由该行中所有单元格的数据组成的列表

print(a)
'''
table.row_slice(rowx)  #返回由该列中所有的单元格对象组成的列表

table.row_types(rowx, start_colx=0, end_colx=None)    #返回由该行中所有单元格的数据类型组成的列表

table.row_values(rowx, start_colx=0, end_colx=None)   #返回由该行中所有单元格的数据组成的列表

table.row_len(rowx) #返回该列的有效单元格长度
复制代码
'''
input()