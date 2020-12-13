from load import ASDAN_EXCEL_REDER
from conduct import ASDAN_ANALYZER
from result import ASDAN_TABLE_STYLE_RENDERING
from assist import MEMORY_CONTROL
from result import TABLE_WRITER
from assist import PERMISSION
import json

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
        print("[CORE] 初始化内存函数")
        if self.cmdlist == []:
            print("[init_memory] 清除全部内存")
            self.path = ""  # 程序路径
            self.data = {}  # 记忆存储 数据
            self.period = "1"  # 记忆存储 周期信息，时间
            self.memo_data = {}  # 记忆存储 变量记忆存储器
            self.ana_data = {}  # 运算时使用的唯一默认存储变量
            # 保存为每最后一次进行的运算结果，用于为下一步运算进行准备
            print("[init_memory] 内存清除完成")

        if "path" in self.cmdlist:
            print("[init_memory] 初始化路径内存")
            self.path = ""  # 程序路径
        if "data" in self.cmdlist:
            print("[init_memory] 初始化核心数据结构")
            self.data = {}  # 记忆存储 数据
        if "period" in self.cmdlist:
            print("[init_memory] 初始化周期时间数据")
            self.period = "1"  # 记忆存储 周期信息，时间
        if "variate" in self.cmdlist:
            print("[init_memory] 初始化memo记忆")
            self.memo_data = {}  # 记忆存储 变量记忆存储器
        if "ana" in self.cmdlist:
            print("[init_memory] 初始化运算结果暂存器")
            self.ana_data = {}


    def start_verify(self):
        permission = PERMISSION()
        if permission.verify_permission():
            return True
        else:
            return False


    def set_period(self):
        print("[CORE] 设置周期函数")
        print("[set_period] 设置周期为 {}".format(self.cmdlist[0]))
        self.period = str(self.cmdlist[0])
        print("[set_period] 周期设置完成")

    def init_data_structure(self):
        # self.cmdlist 中具有一个参数，为数据上限结构
        print("[CORE] 初始化数据结构函数")
        print("[init_data_structure] 正在准备基础数据结构")
        self.data = {
            "city_background_data": {},
            "business_city_data": {}
        }
        print("[init_data_structure] 正在生成 {} 周期数据结构".format(self.cmdlist[0]))
        for i in range(1, int(self.cmdlist[0])+1):
            self.data["city_background_data"][str(i)] = {}
            self.data["business_city_data"][str(i)] = {}
        print("[init_data_structure] 数据结构准备就绪")

    def load_data(self):
        # self.cmdlist 中具有一个参数，为读取的地址，完整文件路径
        print("[CORE] 内存数据读取函数")
        memoryCtrol = MEMORY_CONTROL()
        if self.cmdlist == []:
            print("[load_data] 读取默认位置 ./data.json")
            self.data, self.period, self.memo_data = memoryCtrol.load_data(
                "data.json")
            print("[load_data] 读取完成")
        else:
            print("[load_data] 读取制定位置 {}".format(self.cmdlist[0]))
            self.data, self.period, self.memo_data = memoryCtrol.load_data(
                self.cmdlist[0])
            print("[load_data] 读取完成")

    def save_data(self):
        # self.cmdlist 中具有一个参数，为保存的地址，完整文件路径
        print("[CORE] 内存数据保存函数")
        print("[save_data] 传入现有数据")
        memoryCtrol = MEMORY_CONTROL()
        memoryCtrol.data = self.data
        memoryCtrol.period = self.period
        memoryCtrol.memo_data = self.memo_data
        
        if self.cmdlist == []:
            print("[save_data] 保存默认位置 data.json")
            memoryCtrol.save_data("data.json")
            print("[save_data] 保存成功")
        else:
            print("[save_data] 保存指定位置 {}".format(self.cmdlist[0]))
            memoryCtrol.save_data(self.cmdlist[0])
            print("[save_data] 保存成功")

    def read_table(self):
        # 用于读取ASDANEXCEL　表格的函数
        print("[CORE] 表格读取函数")
        if self.cmdlist[0] == "city":  # city table sign
            print("[read_table] 运行表格读取器 “city”")
            asdanExcelReader = ASDAN_EXCEL_REDER()
            asdanExcelReader.path = self.cmdlist[1]
            asdanExcelReader.data = self.data
            asdanExcelReader.period = self.period
            self.data = asdanExcelReader.asdan_city_table()
            print("[read_table] 读取完成，已存入 核心data数据")

        if self.cmdlist[0] == "fcity":
            print("[read_table] 运行表格读取器 “fast_city”")
            asdanExcelReader = ASDAN_EXCEL_REDER()
            asdanExcelReader.path = self.cmdlist[1]
            asdanExcelReader.data = self.data
            asdanExcelReader.period = self.period
            self.data = asdanExcelReader.fast_asdan_city_table()
            print("[read_table] 读取完成，已存入 核心data数据")

    def memo(self):
        # 用于进行程序内部变量存储的函数
        print("[CORE] MEMO 内存控制函数")
        if self.cmdlist[0] == "add":
            print("[memo] 添加字典内存 键：{}".format(self.cmdlist[1]))
            self.memo_data[self.cmdlist[1]] = self.ana_data

        if self.cmdlist[0] == "del":
            print("[memo] 删除字典内存 键：{}".format(self.cmdlist[1]))
            del self.memo_data[self.cmdlist[1]]

    def analyzer(self):
        # 算法
        # 一个参数，指定 使用的算法
        print("[CORE] analyzer核心算法函数")
        if self.cmdlist[0] == "JCT":
            print("[analyzer] 运行算法 'JASON_TEAM_CITY_TABlE_ANA' ")
            ana = ASDAN_ANALYZER()
            ana.data = self.data
            ana.period = self.period
            self.ana_data = ana.Jason_team_city_table_ana()
            print("[analyzer] 算法执行完成，结果已存入 ana_data")


    def table_style_rendering(self):
        #表格样式渲染器
        #cmdlist 可选填入，如果有参数，将会是memo的索引
        print("[CORE] 表格样式渲染器")
        if self.cmdlist[0] == "JCT":
            print("[table_style_rendering] 运行算法 'JASON_TEAM_CITY_TABlE_REN' ")
            tsr = ASDAN_TABLE_STYLE_RENDERING()
            if len(self.cmdlist) > 1:
                tsr.data = self.memo_data[self.cmdlist[1]]
            else:
                tsr.data = self.ana_data
            self.ana_data = tsr.Jason_team_city_table_ren()
            print("[table_style_rendering] 表格渲染完成，结果已存入 ana_data")
            

    def table_writer(self):
        '''
        表格写入器，此函数具有相对较为特殊的参数传入机制
        cmdlist 具有两个参数，分别为 表格绝对路径 和 memo命令控制器
        '''
        print("[CORE] 表格生成器")
        data = {}
        data["file_path"] = self.cmdlist[0]
        data["shells"] = []
        if len(self.cmdlist) > 1:
            if self.cmdlist[1] == "memo":
                print("[table_writer] memo 内存提取器")
                print("[table_writer] 已存储的变量（注意请选择可绘制数据）：")
                js = 0
                data_of_memo = {}
                for name, memo_detail in self.memo_data.items():
                    js += 1
                    data_of_memo[str(js)] = memo_detail
                    print("[table_writer]  {} 变量名 {}".format(str(js),name))
                
                while True:
                    shell_data_dic = {}
                    number = input("[table_writer] 输入编号选择（输入q退出）：")
                    if number == "q":
                        break
                    name = input("[table_writer] 表格名称：")
                    shell_data_dic["name"] = name
                    shell_data_dic["data"] = data_of_memo[number]
                    data["shells"].append(shell_data_dic)
        else:
            shell_data_dic = {}
            name = input("[table_writer] 表格名称：")
            shell_data_dic["name"] = name
            shell_data_dic["data"] = self.ana_data
            data["shells"].append(shell_data_dic)

        table = TABLE_WRITER()
        table.table_data = data
        table.write()
        print("[table_writer] 执行完成")
    
    

    def list_memory(self):
        # 用于输出程序内部变量的函数
        print("[CORE] 内存预览函数")
        if self.cmdlist[0] == "g":
            if "path" in self.cmdlist or len(self.cmdlist) == 1:
                if self.path != "":
                    print("[程序内部变量] self.path 存在并已使用")
                else:
                    print("[程序内部变量] self.path 没有被定义和使用")
            if "data" in self.cmdlist or len(self.cmdlist) == 1:
                if self.data != {}:
                    print("[程序内部变量] self.data 存在并已使用")
                else:
                    print("[程序内部变量] self.data 没有被定义和使用")
            if "period" in self.cmdlist or len(self.cmdlist) == 1:
                if self.period != "1":
                    print("[程序内部变量] self.period 值为{}".format(self.period))
                else:
                    print("[程序内部变量] self.period 值为1 初始值")
            if "variate" in self.cmdlist or len(self.cmdlist) == 1:
                if self.memo_data != {}:
                    print("[程序内部变量] self.memo 已被使用")
                    print("其结构键含有：")
                    for key_name in self.memo_data.keys():
                        print("[memo 内键] {}".format(key_name))
                else:
                    print("[程序内部变量] self.memo 没有被定义和使用")
            if "ana" in self.cmdlist or len(self.cmdlist) == 1:
                if self.ana_data != {}:
                    print("[程序内部变量] self.ana_data 存在并已使用")
                else:
                    print("[程序内部变量] self.ana_data 没有被定义和使用")

        if self.cmdlist[0] == "d": 
            if "path" in self.cmdlist or len(self.cmdlist) == 1:
                if self.path != "":
                    print("[程序内部变量] self.path 存在并已使用")
                    print("[变量值] {}".format(self.path))
                else:
                    print("[程序内部变量] self.path 没有被定义和使用")
            if "period" in self.cmdlist or len(self.cmdlist) == 1:
                if self.period != "1":
                    print("[程序内部变量] self.period 值为{}".format(self.period))
                    print("[变量值] {}".format(self.period))
                else:
                    print("[程序内部变量] self.period 值为1 初始值")
            if "variate" in self.cmdlist or len(self.cmdlist) == 1:
                if self.memo_data != {}:
                    print("[程序内部变量] self.memo 已被使用")
                    input("按下任意键 输出memo数据结构")
                    data = json.dumps(self.memo_data, indent=4,ensure_ascii=False, sort_keys=False,separators=(',', ':'))
                    print(data)
                else:
                    print("[程序内部变量] self.memo 没有被定义和使用")
            if "ana" in self.cmdlist or len(self.cmdlist) == 1:
                if self.ana_data != {}:
                    print("[程序内部变量] self.ana_data 存在并已使用")
                    input("按下任意键 输出ana_data数据结构")
                    data = json.dumps(self.ana_data, indent=4,ensure_ascii=False, sort_keys=False,separators=(',', ':'))
                    print(data)
                else:
                    print("[程序内部变量] self.ana_data 没有被定义和使用")
            if "data" in self.cmdlist or len(self.cmdlist) == 1:
                if self.data != {}:
                    print("[程序内部变量] self.data 存在并已使用")
                    input("按下任意键 输出data数据结构")
                    data = json.dumps(self.data, indent=4,ensure_ascii=False, sort_keys=False,separators=(',', ':'))
                    print(data)
                else:
                    print("[程序内部变量] self.data 没有被定义和使用")
