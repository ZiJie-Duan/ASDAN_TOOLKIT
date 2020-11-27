

class CORE_CONTROL():
    """
    用于操控底层函数的驱动类
    """
    def __init__(self):
        self.path = "" #程序路径
        self.data = {} #记忆存储 数据
        self.period = "1"  #记忆存储 周期信息，时间
        self.variate_data = {}  #记忆存储 变量记忆存储器
        self.cmdlist = [] #命令参数列表


    def init_all_memory(self):
        self.path = "" #程序路径
        self.data = {} #记忆存储 数据
        self.period = "1"  #记忆存储 周期信息，时间
        self.variate_data = {}  #记忆存储 变量记忆存储器
        self.cmdlist = [] #命令参数列表

    def set_period(self,aim_period):
        self.period = str(aim_period)



class MEMORY_CONTROL():
    """
    负责程序本体记忆
    保存与读取
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


	def save_data(self,save_mode):
		