from analyzer import ASDAN_ANALYZER
from memorizer import MEMORY_CONTROL
from loader import ASDAN_EXCEL_LOADER
from setting import SETTING 
from writer import TABLE_WRITER


class CORE_DRIVE():
    """
    ASDAN V2.0 core drive
    """

    def __init__(self):
        self.cmdlist = []
        self.set = SETTING()
        self.memo = MEMORY_CONTROL()
        self.loader = ASDAN_EXCEL_LOADER()
        self.analyzer = ASDAN_ANALYZER()
        self.writer = TABLE_WRITER()

        self.memo.set = self.set
        self.loader.memo = self.memo
        self.loader.set = self.set
        self.analyzer.memo = self.memo
        self.analyzer.set = self.set
        self.writer.memo = self.memo
        self.writer.set = self.set

    def path_clean(self,path):
        # this function is used to remove the quotes on two side of path
        if path[0] == "'" or path[0] == '"':
            return path[1:-1]
        else:
            return path
    

    def load_data(self):
        if len(self.cmdlist) == 0:
            print("[core] load data from database")
            self.memo.load_data()
            print("[core] Finish")
        elif len(self.cmdlist) == 1:
            path = self.path_clean(self.cmdlist[0])
            print("[core] load data from {}".format(path))
            self.set.path_of_database = path
            self.memo.load_data()
            print("[core] Finish")

    def save_data(self):
        if len(self.cmdlist) == 0:
            print("[core] save data to database")
            self.memo.save_data()
            print("[core] Finish")
        elif len(self.cmdlist) == 1:
            path = self.path_clean(self.cmdlist[0])
            print("[core] save data to {}".format(path))
            self.set.path_of_database = path
            self.memo.save_data()
            print("[core] Finish")

    def load_table(self):
        path = self.path_clean(self.cmdlist[0])
        print("[core] load table from {}".format(path))
        self.set.path_of_original_table = path
        self.loader.asdan_city_loader()
        print("[core] Finish")

    def analyze_data_normal(self):
        print("[core] analyze data")
        self.analyzer.asdan_normal_table_ana()
        print("[core] Finish")

    def write_table(self):
        path = self.path_clean(self.cmdlist[1])
        print("[core] write result {} data to {}".format(self.cmdlist[0],path))
        self.set.path_of_result_table = path
        self.writer.write(name=self.cmdlist[0])
        print("[core] Finish")

    def transfer_data(self):
        if len(self.cmdlist) == 2:
            print("[core] transfer data to {}".format(self.cmdlist[0]+" "+self.cmdlist[1]))
            self.memo.transfer_data(mod="temporary_data to databese",\
                group=self.cmdlist[0],name=self.cmdlist[1])
            print("[core] Finish")
        elif len(self.cmdlist) == 4:
            print("[core] internal transfer data from {} to {}"\
                .format(self.cmdlist[0]+" "+self.cmdlist[1],self.cmdlist[2]+" "+self.cmdlist[3]))
            self.memo.transfer_data(mod="database to database",\
                group=self.cmdlist[0],name=self.cmdlist[1],\
                    group2=self.cmdlist[2],name2=self.cmdlist[3])
            print("[core] Finish")

    def show_memory(self):
        self.memo.show_memory()

    def del_data(self):
        if self.cmdlist[0] == "t":
            print("[core] del data '{}' group".format(self.cmdlist[0]))
            self.memo.del_data(group=self.cmdlist[0])
            print("[core] Finish")
        else:
            print("[core] del data '{}' form '{}' group".format(self.cmdlist[1],self.cmdlist[0]))
            self.memo.del_data(group=self.cmdlist[0],name=self.cmdlist[1])
            print("[core] Finish")

    def change_period(self):
        print("[core] change period to {}".format(self.cmdlist[0]))
        self.memo.change_period(period=self.cmdlist[0])
        print("[core] Finish")