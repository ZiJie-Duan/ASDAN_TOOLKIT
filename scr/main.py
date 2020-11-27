#ASDAN 商赛辅助分析程序
from load import ASDAN_EXCEL_REDER



test = ASDAN_EXCEL_REDER()


test.path = r"C:\Users\lucyc\Desktop\ASDAN_TOOLKIT\数据输入表格.xlsx"
test.data = {"city_background_data":{"1":{}},"business_city_data":{"1":{}}}
test.period = "1"
test.init_table()
b = test.asdan_city_table()

print(b)
input()