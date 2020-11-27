import xlrd
import traceback


class ASDAN_EXCEL_REDER():
	"""
	用于读取ASDAN商赛的excel电子表格的底层函数
	"""

	def __init__(self,path=None,global_information=None,\
		business_information=None,period=None):

		self.path = path
		self.global_information = global_information
		self.business_information = business_information
		self.tables_data = None
		self.period = period
	
	def init_table(self):
		self.tables_data = xlrd.open_workbook(self.path)


	#TRA [Translator] 定义
	def asdan_city_table(self):	#阿斯丹 标准城市报表读取器
		
		tables_name = self.tables_data.sheet_names()

		#判断带有识别码 “CITY”的表格，并加入到待处理列表
		aim_tables_name = []
		for table_name in tables_name:
			if "CITY" in table_name:
				aim_tables_name.append(table_name)
		
		#进行表格循环数据提取	
		for aim_table_name in aim_tables_name:
			#初始化临时数据结构
			global_information = {}
			table = self.tables_data.sheet_by_name(aim_table_name)
			#获取表格内有效行数
			number_of_rows = table.nrows

			#构建global_information 数据结构
			city_name = table.cell_value(1,0)
			global_information["Population"] = table.cell_value(1,1)
			global_information["Penetration"] = table.cell_value(1,2)
			global_information["Market_Size"] = table.cell_value(1,3)
			global_information["Total_Sales_Volume"] = table.cell_value(1,4)
			global_information["Avg_Price"] = table.cell_value(1,5)
			self.global_information[self.period][city_name] = global_information

			#构建business_information 数据结构
			for rows_index in range(number_of_rows):
				if rows_index > 2:
					business_information = {}
					line_data = table.row_values(rows_index, start_colx=0, end_colx=None)
					team_name = line_data[0]
					business_information["Agents"] = line_data[1]
					business_information["Marketing_Investment"] = line_data[2]
					business_information["Product_Quality_Index"] = line_data[3]
					business_information["Price"] = line_data[4]
					business_information["Sales_Volume"] = line_data[5]
					business_information["Market_Share"] = line_data[6]

					#防止发生队伍数据覆盖写入，在队伍不存在时，加入队伍名称，如果存在，则不操作
					if team_name not in self.business_information[self.period]:
						self.business_information[self.period][team_name] = {}
					self.business_information[self.period][team_name][city_name] = business_information
			
		return self.global_information,self.business_information


'''
		try:
			
		except:
			traceback.print_exc()#错误捕捉器
'''