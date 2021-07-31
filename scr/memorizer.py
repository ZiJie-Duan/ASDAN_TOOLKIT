import json

class MEMORY_CONTROL():
    """
    this class uses to store the memory of the whole program.
    it can store three types of data.
    1, original data
    2, processed data
    3, graphical data
    """

    def __init__(self):
        self.set = None
        self.original_data = {
            "1" : {}
        } # this variate only can be changed by the loader of tables.
        # the processed data and grahical data only can be gived by temporary data.
        self.processed_data = {}
        self.graphical_data = {}
        self.period = "1" # round of game
        self.temporary_data = {}  # temporary storage


    def load_data(self):
        # this function is used for loading all the data.
        # it will remove the data of the memory of program
        all_data = []
        with open(self.set.path_of_database) as content:
            all_data = json.load(content)

        self.original_data = all_data[0]
        self.processed_data = all_data[1]
        self.graphical_data = all_data[2]
        self.period = all_data[3]
        self.temporary_data = all_data[4]


    def save_data(self):
        # this function is used for saving all the data.
        all_data = [self.original_data, self.processed_data, self.graphical_data,\
            self.period, self.temporary_data]
        with open(self.set.path_of_database, 'w') as content:
            json.dump(all_data, content)


    def add_city_original_data(self,data):
        # this function is used to insert the city data to the original data.
        for key in data.keys():
            # identify whether here already insert the business name in the original data. 
            if key in self.original_data[self.period]:
                break
            else:
                self.original_data[self.period][key] = data[key]

    
    def show_memory(self):
        print("\n------------MEMORY------------")
        print("\n-----original_data占用情况-----")
        for period, data in self.original_data.items():
            if data == {}:
                print("周期：{} 数据为空".format(period))
            else:
                print("周期：{} 数据存在".format(period))
        print("\n-----processed_data占用情况-----")
        for name, _ in self.processed_data.items():
            print("'{}' 数据存在".format(name))
        print("\n-----graphical_data占用情况-----")
        for name, _ in self.graphical_data.items():
            print("'{}' 数据存在".format(name))
        print("\n-----temporary_data占用情况-----")
        if self.temporary_data == {}:
            print("缓存数据不存在")
        else:
            print("缓存数据存在")
        print("")


    def transfer_data(self,mod,group,name,group2="",name2=""):
        if mod == "temporary_data to databese":
            if group == "p":
                self.processed_data[name] = self.temporary_data
            elif group == "g":
                self.graphical_data[name] = self.temporary_data
        elif mod == "database to database":
            if group == "p":
                if group2 == "p":
                    self.processed_data[name2] = self.processed_data[name]
                elif group2 == "g":
                    self.graphical_data[name2] = self.processed_data[name]
            elif group == "g":
                if group2 == "p":
                    self.processed_data[name2] = self.graphical_data[name]
                elif group2 == "g":
                    self.graphical_data[name2] = self.graphical_data[name]


    def del_data(self,group,name):
        if group == "p":
            del self.processed_data[name]
        elif group == "g":
            del self.graphical_data[name]
        elif group == "o":
            del self.original_data[name]
        elif group == "t":
            self.temporary_data = {}

    
    def change_period(self,period):
        # this function is used to create data structure automatically
        if period in self.original_data:
            self.period = period
        else:
            self.original_data[period] = {}

