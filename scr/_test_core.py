from analyzer import ASDAN_ANALYZER
from memorizer import MEMORY_CONTROL
from loader import ASDAN_EXCEL_LOADER
from setting import Setting
from writer import TABLE_WRITER

set = Setting()
memo = MEMORY_CONTROL()
memo.set = set
table = ASDAN_EXCEL_LOADER()
table.set = set
table.memo = memo
set.path_of_original_table = r"C:\Users\Peter Duan\Desktop\aaaaaaaaaaaaaaaaaaa.xls"
set.path_of_database_auto = r"C:\Users\Peter Duan\Desktop\auto_save_databace.json"
set.path_of_result_table = r"C:\Users\Peter Duan\Desktop\bbbbbbbbbbbbbba.xls"
table.asdan_city_loader()
print(memo.original_data)

ana = ASDAN_ANALYZER()
ana.memo = memo
ana.set = set

ana.asdan_normal_table_ana()


writer = TABLE_WRITER()
writer.memo = memo
writer.set = set

writer.write()
