import json
from load import ASDAN_EXCEL_REDER


class MEMORY_CONTROL():
    """
    负责程序本体记忆
    保存与读取
    """

    def __init__(self):
        self.data = {}  # 记忆存储 数据
        self.period = "1"  # 记忆存储 周期信息，时间
        self.memo_data = {}  # 记忆存储 变量记忆存储器

    def save_data(self, save_path):
        # 全部存储模式
        save_data_final = [self.data, self.period, self.memo_data]
        with open(save_path, 'w') as content:
            json.dump(save_data_final, content)

    def load_data(self, load_path):
        # 全部读取模式
        all_data = []
        with open(load_path) as content:
            all_data = json.load(content)
        self.data = all_data[0]
        self.period = all_data[1]
        self.memo_data = all_data[2]

        return self.data, self.period, self.memo_data


class CORE_CONTROL():
    """
    用于操控底层函数的驱动类
    """

    def __init__(self):
        self.path = ""  # 程序路径
        self.data = {}  # 记忆存储 数据
        self.period = "1"  # 记忆存储 周期信息，时间
        self.memo_data = {}  # 记忆存储 变量记忆存储器
        self.ana_data = {}  # 运算时使用的唯一默认存储变量
        # 保存为每最后一次进行的运算结果，用于为下一步运算进行准备
        self.cmdlist = []

    def init_memory(self):
        if self.cmdlist == []:
            self.path = ""  # 程序路径
            self.data = {}  # 记忆存储 数据
            self.period = "1"  # 记忆存储 周期信息，时间
            self.memo_data = {}  # 记忆存储 变量记忆存储器
            self.ana_data = {}  # 运算时使用的唯一默认存储变量
            # 保存为每最后一次进行的运算结果，用于为下一步运算进行准备

        if "path" in self.cmdlist:
            self.path = ""  # 程序路径
        if "data" in self.cmdlist:
            self.data = {}  # 记忆存储 数据
        if "period" in self.cmdlist:
            self.period = "1"  # 记忆存储 周期信息，时间
        if "variate" in self.cmdlist:
            self.memo_data = {}  # 记忆存储 变量记忆存储器
        if "ana" in self.cmdlist:
            self.ana_data = {}

    def set_period(self):
        self.period = str(self.cmdlist[0])

    def init_data_structure(self):
        # self.cmdlist 中具有一个参数，为数据上限结构
        self.data = {
            "city_background_data": {},
            "business_city_data": {}
        }
        for i in range(1, int(self.cmdlist[0])+1):
            self.data["city_background_data"][str(i)] = {}
            self.data["business_city_data"][str(i)] = {}

    def load_data(self):
        # self.cmdlist 中具有一个参数，为读取的地址，完整文件路径
        memoryCtrol = MEMORY_CONTROL()
        if self.cmdlist == []:
            self.data, self.period, self.memo_data = memoryCtrol.load_data(
                "data.json")
        else:
            self.data, self.period, self.memo_data = memoryCtrol.load_data(
                self.cmdlist[0])

    def save_data(self):
        # self.cmdlist 中具有一个参数，为保存的地址，完整文件路径
        memoryCtrol = MEMORY_CONTROL()
        memoryCtrol.data = self.data
        memoryCtrol.period = self.period
        memoryCtrol.result_list = self.memo_data
        if self.cmdlist == []:
            memoryCtrol.save_data("data.json")
        else:
            memoryCtrol.save_data(self.cmdlist[0])

    def read_table(self):
        # 用于读取ASDANEXCEL　表格的函数
        if self.cmdlist[1] == "city":  # city table sign
            asdanExcelReader = ASDAN_EXCEL_REDER()
            asdanExcelReader.path = self.cmdlist[0]
            asdanExcelReader.data = self.data
            asdanExcelReader.period = self.period
            self.data = asdanExcelReader.asdan_city_table()

    def memo(self):
        # 用于进行程序内部变量存储的函数
        if self.cmdlist[0] == "add":
            self.memo_data[self.cmdlist[1]] = self.ana_data

        if self.cmdlist[0] == "del":
            del self.memo_data[self.cmdlist[1]]

    def list_all_memory(self):
        # 用于输出程序内部变量的函数
        if self.cmdlist[0] == "general" or self.cmdlist == []:
            if self.cmdlist[1] 
