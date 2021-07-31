import xlwt

        
class TABLE_WRITER():

    def __init__(self):
        self.memo = None
        self.set = None

    def write(self,name):
        # 创建一个workbook 设置编码
        workbook = xlwt.Workbook(encoding = 'utf-8')
        worksheet = workbook.add_sheet("data")

        for point_data in self.memo.graphical_data[name]:

            worksheet.write(point_data[0],point_data[1], label = point_data[2])

        # 保存
        #workbook.save('Excel_test.xls')
        workbook.save(self.set.path_of_result_table)

