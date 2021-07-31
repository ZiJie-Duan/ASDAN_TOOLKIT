import xlrd
import difflib
from setting import SETTING
from memorizer import MEMORY_CONTROL


class ASDAN_EXCEL_LOADER():
	"""
	this class is used to load the reports of citys.
	we provide only one type of loaders now "asdan_city_report"
	"""

	def __init__(self):
		self.memo = None # here import the class "memorizer" to access the moemory.
		self.set = None # here import the calss "setting" to access the basic setting.


	def asdan_city_loader(self):
		# ASDAN normal fast
		# intelligently and apace load the city report.
		# this is the third generation loader.

		# get table data 
		tables_data = xlrd.open_workbook(self.set.path_of_original_table)
		# load the table witch named "CITY"
		table = tables_data.sheet_by_name("CITY")

		row = 0
		while row < table.nrows:
			if "Market Report" in str(table.cell_value(row,0)):
				input(str(table.cell_value(row,0)))
				#开始准备城市背景报表
				final_data = {}
				city_background_information = {}
				teams_imformation = {}

				city_name = table.cell_value(row,0)[16:]
				row += 3
				line_data = table.row_values(row, start_colx=0, end_colx=None)
				line_data = [i for i in line_data if i != '']

				city_background_information["Population"] = line_data[0]
				city_background_information["Penetration"] = line_data[1]
				city_background_information["Market_Size"] = line_data[2]
				city_background_information["Total_Sales_Volume"] = line_data[3]
				city_background_information["Avg_Price"] = line_data[4]

				row += 2 # 定位城市报表内容信息
				while True:
					try:
						if "Market Report" in str(table.cell_value(row,0)):
							break
					except IndexError:
						break

					# here use to check whether cell is empty.
					if str(table.cell_value(row,0)) != "": # if the cell is not empty
									
						line_data = table.row_values(row, start_colx=0, end_colx=None)
						team_name = line_data[0]
						teams_imformation_details = {}
						teams_imformation_details["Agents"] = line_data[1]
						teams_imformation_details["Marketing_Investment"] = line_data[2]
						teams_imformation_details["Product_Quality_Index"] = line_data[3]
						teams_imformation_details["Price"] = line_data[4]
						teams_imformation_details["Sales_Volume"] = line_data[5]
						teams_imformation_details["Market_Share"] = line_data[6]

						teams_imformation[team_name] = teams_imformation_details
						row += 1
					else: # if the cell is empty
						# then we need to push one row.
						row += 1

				final_data[city_name] = {
					"city_background_information" : city_background_information,
					"teams_imformation" : teams_imformation
				}

				self.memo.add_city_original_data(data=final_data)
			else:
				row += 1



