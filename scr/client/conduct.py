
class ASDAN_ANALYZER():

    def __init__(self):
        self.data = {} #用于运算的输入数据
        self.result = {} #运算完成的表格绘制数据
        self.period = "1"

    def Jason_team_city_table_ana(self):
        #用于绘制JASON定制的 商赛 队伍城市表格的算法

        #提取基础信息
        back_ground_data = self.data["city_background_data"][self.period]
        business_city_data = self.data["business_city_data"][self.period]

        table_style = {
            "first_row" : [],
            "first_col" : []
        }
        avg_price = {}
        for city_name, detail in back_ground_data.items():
            table_style["first_row"].append(city_name)
            avg_price[city_name] = detail["Avg_Price"]
        
        total_salse = {}
        table_content = []
        #顺序获取公司信息
        for business_code, detail in business_city_data.items():
            table_style["first_col"].append(business_code)
            business_total_sales_volume = 0
            for city_name, business_city_detail in detail.items():
                business_total_sales_volume += business_city_detail["Sales_Volume"]
                table_content_son = [city_name,business_code,business_city_detail]
                table_content.append(table_content_son)
            
            total_salse[business_code] = business_total_sales_volume
        
        revenue = {}
        for business_code, detail in business_city_data.items():
            total_revenue = 0
            for city_name, business_city_detail in detail.items():
                price = business_city_detail["Price"]
                sales_volume = business_city_detail["Sales_Volume"]
                total_revenue += price*sales_volume
            revenue[business_code] = total_revenue

        self.result["table_style"] = table_style
        self.result["content"] = table_content
        self.result["avg_price"] = avg_price
        self.result["total_salse"] = total_salse
        self.result["revenue"] = revenue
        return self.result