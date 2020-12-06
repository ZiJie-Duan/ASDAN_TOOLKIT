import xlwt

class ASDAN_TABLE_STYLE_RENDERING():

    def __init__(self):
        self.data = {}
        self.result = {}

    def Jason_team_city_table_ren(self):
        point_location = {
            "row":{},
            "col":{}
            }
        table_style = self.data["table_style"]

        #核心数据绘制点位 列表
        point_location_data = [] #三个元素，第一个为行，第二个为列，第三个为值

        #将两组数据绘制入定位表中
        #这里有一些抽象，First——row 在table_style中的意思是第一行的值
        #而定位表中的Row 意思是 表中每一列的坐标 位置
        location = 1
        for location_sign in table_style["first_row"]:
            point_location["col"][location_sign] = location
            #加入点位绘制列表，注意，这个循环绘制的是水平方向的数值，所以，location为列
            point_location_data.append([0,int(location),location_sign])
            location += 6
        location = 2
        for location_sign in table_style["first_col"]:
            point_location["row"][location_sign] = location
            #加入点位绘制列表，注意，这个循环绘制的是竖直方向的数值，所以，location为行
            point_location_data.append([int(location),0,location_sign])
            location += 1
        
        for city_name, avg_price in self.data["avg_price"].items():
            col = point_location["col"][city_name]
            row = 0
            #绘制平均价格到表格中
            point_location_data.append([row,col+1,"Avg.Price"])
            point_location_data.append([row,col+2,avg_price])
        
        
        for _, col in point_location["col"].items():
            point_location_data.append([1,col,"Agents"])
            point_location_data.append([1,col+1,"Marketing_Investment"])
            point_location_data.append([1,col+2,"Product_Quality_Index"])
            point_location_data.append([1,col+3,"Price"])
            point_location_data.append([1,col+4,"Sales_Volume"])
            point_location_data.append([1,col+5,"Market_Share"])

        for detail in self.data["content"]:
            #描点数据填充
            #注意加入表格读入大小写统一
            col = point_location["col"][detail[0]]
            row = point_location["row"][detail[1]]
            point_location_data.append([row,col,detail[2]["Agents"]])
            point_location_data.append([row,col+1,detail[2]["Marketing_Investment"]])
            point_location_data.append([row,col+2,detail[2]["Product_Quality_Index"]])
            point_location_data.append([row,col+3,detail[2]["Price"]])
            point_location_data.append([row,col+4,detail[2]["Sales_Volume"]])
            point_location_data.append([row,col+5,detail[2]["Market_Share"]])
        
        
        return point_location_data
        
        
class TABLE_WRITER():

    def __init__(self):
        self.table_data = {}

    def write(self):
        # 创建一个workbook 设置编码
        workbook = xlwt.Workbook(encoding = 'utf-8')
        # cmdlist memo, path
        #memo 命令需要特殊解析
        for table in self.table_data["shells"]:
            # 创建一个worksheet
            worksheet = workbook.add_sheet(table["name"])
            for point_data in table["data"]:
                # 写入excel
                # 参数对应 行, 列, 值
                worksheet.write(point_data[0],point_data[1], label = point_data[2])
        # 保存
        #workbook.save('Excel_test.xls')
        workbook.save(self.table_data["file_path"])

