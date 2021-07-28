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
        self.original_data = {} # this variate only can be changed by the loader of tables.
        # the processed data and grahical data only can be gived by temporary data.
        self.processed_data = {}
        self.graphical_data = {}
        self.period = "1"  # round of game
        self.temporary_data = {}  # temporary storage


    def load_data(self):
        # this function is used for loading all the data.
        # it will remove the data of the memory of program
        all_data = []
        with open(self.set.database_path) as content:
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
        with open(self.set.database_path, 'w') as content:
            json.dump(all_data, content)
    

    def auto_save_data(self):
        # this function is used for saving all the data automatically.
        all_data = [self.original_data, self.processed_data, self.graphical_data,\
            self.period, self.temporary_data]
        databace_path = self.set.database_path[:-5] + "_autosave_.json"
        with open(databace_path, 'w') as content:
            json.dump(all_data, content)
    
    
    def transfer_data(self):
        


