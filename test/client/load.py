import xlrd


class ASDAN_EXCEL_REDER():
	"""
	用于读取ASDAN商赛的excel电子表格的底层函数
	"""

	def __init__(self,path=None,data=None,period=None):
		self.path = path
		self.data = data
		self.period = period
	

	#TRA [Translator] 定义
	def asdan_city_table(self):	#阿斯丹 标准城市报表读取器

		tables_data = xlrd.open_workbook(self.path)
		
		tables_name = tables_data.sheet_names()

		#判断带有识别码 “CITY”的表格，并加入到待处理列表
		aim_tables_name = []
		for table_name in tables_name:
			if "CITY" in table_name:
				aim_tables_name.append(table_name)
		
		#进行表格循环数据提取	
		for aim_table_name in aim_tables_name:
			#初始化临时数据结构
			city_background_data = {}
			table = tables_data.sheet_by_name(aim_table_name)
			#获取表格内有效行数
			number_of_rows = table.nrows

			#构建city_background_data 数据结构
			city_name = table.cell_value(1,0)
			city_background_data["Population"] = table.cell_value(1,1)
			city_background_data["Penetration"] = table.cell_value(1,2)
			city_background_data["Market_Size"] = table.cell_value(1,3)
			city_background_data["Total_Sales_Volume"] = table.cell_value(1,4)
			city_background_data["Avg_Price"] = table.cell_value(1,5)
			self.data["city_background_data"][self.period][city_name] = city_background_data

			#构建business_city_data 数据结构
			for rows_index in range(number_of_rows):
				if rows_index > 2:
					business_city_data = {}
					line_data = table.row_values(rows_index, start_colx=0, end_colx=None)
					team_name = line_data[0]
					business_city_data["Agents"] = line_data[1]
					business_city_data["Marketing_Investment"] = line_data[2]
					business_city_data["Product_Quality_Index"] = line_data[3]
					business_city_data["Price"] = line_data[4]
					business_city_data["Sales_Volume"] = line_data[5]
					business_city_data["Market_Share"] = line_data[6]

					#防止发生队伍数据覆盖写入，在队伍不存在时，加入队伍名称，如果存在，则不操作
					if team_name not in self.data["business_city_data"][self.period]:
						self.data["business_city_data"][self.period][team_name] = {}
					self.data["business_city_data"][self.period][team_name][city_name] = business_city_data
			
		return self.data


	def fast_asdan_city_table(self):
		#阿斯丹 标准 快速城市报表读取器

		#获取表格信息位置
		tables_data = xlrd.open_workbook(self.path)
		#加载名为CITY的表格
		table = tables_data.sheet_by_name("CITY")

		#每一个信息快在表格中的位置，起始位置和终止位置
		start_point_row = []

		#检测表格中的开始结束标识
		for row in range(table.nrows):
			if table.cell_value(row,0) == "SHEET_START":
				start_point_row.append(row)

		#开始准备城市背景报表
		city_background_data = {}
		for row in start_point_row:
			if row == start_point_row[-1]:
				break
			city_name = table.cell_value(row+1,0)
			city_background_data["Population"] = table.cell_value(row+3,0)
			city_background_data["Penetration"] = table.cell_value(row+3,1)
			city_background_data["Market_Size"] = table.cell_value(row+3,2)
			city_background_data["Total_Sales_Volume"] = table.cell_value(row+3,3)
			city_background_data["Avg_Price"] = table.cell_value(row+3,4)
			self.data["city_background_data"][self.period][city_name] = city_background_data

			location_row = row + 4 #定位城市报表内容信息
			while True:
				location_row += 1
				if location_row in start_point_row:
					break
				business_city_data = {}
				line_data = table.row_values(location_row, start_colx=0, end_colx=None)
				team_name = line_data[0]
				business_city_data["Agents"] = line_data[1]
				business_city_data["Marketing_Investment"] = line_data[2]
				business_city_data["Product_Quality_Index"] = line_data[3]
				business_city_data["Price"] = line_data[4]
				business_city_data["Sales_Volume"] = line_data[5]
				business_city_data["Market_Share"] = line_data[6]

				#防止发生队伍数据覆盖写入，在队伍不存在时，加入队伍名称，如果存在，则不操作
				if team_name not in self.data["business_city_data"][self.period]:
					self.data["business_city_data"][self.period][team_name] = {}
				self.data["business_city_data"][self.period][team_name][city_name] = business_city_data
		
		return self.data
