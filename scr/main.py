#ASDAN 商赛辅助分析程序

class CORE_CONTROL():
    """
    用于操控底层函数的驱动类
    """

    def __init__(self,path=None,global_information=None,\
        business_information=None,period=None,translator=None,analyzer=None,\
        rendering=None,variate_data=None,cmdlist=None):
        self.path = path #程序路径
        self.global_information = global_information #记忆存储 全局信息
        self.business_information = business_information  #记忆存储 公司信息
        self.period = period  #记忆存储 周期信息，时间
        self.translator = translator #翻译器
        self.analyzer = analyzer #运算器
        self.rendering = rendering #绘制器
        self.variate_data = variate_data  #记忆存储 变量记忆存储器
        self.cmdlist = cmdlist #命令参数列表

    def init_all_memory(self):
        self.path = None
        self.global_information = None
        self.business_information = None
        self.period = None
        self.translator = None
        self.analyzer = None
        self.rendering = None
        self.variate_data = None
        self.cmdlist = None

    def set_period(self,aim_period):
        self.period = str(aim_period)


    



def cmd_control(cmd,cmdlist):


    


test = ASDAN_EXCEL_REDER()

g = {"1":{}}
b = {"1":{}}
test.path = r"C:\Users\lucyc\Desktop\ASDAN_TOOLKIT\数据输入表格.xlsx"
test.global_information = g
test.business_information = b
test.period = "1"
test.init_table()
g,b = test.asdan_city_table()
print(g)
print(b)
input()