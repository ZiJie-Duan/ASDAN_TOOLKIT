import json

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

