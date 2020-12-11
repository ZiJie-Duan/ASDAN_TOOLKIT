import json
import socket

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


class PERMISSION():

    def __init__(self):
        self.host = "http://asdan.top"
        self.port = 2333
        self.data = "ASDAN_normal"
    
    def verify_permission(self):
        try:
            print("[verify_permission] 初始化程序自检")
            # 创建 socket 对象
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            # 连接服务，指定主机和端口
            s.connect((self.host, self.port))

            s.send(self.data.encode('utf-8'))
            # 接收小于 1024 字节的数据
            msg = s.recv(1024).decode()
            s.close()

            if msg == "TRUE":
                print("[verify_permission] 程序自检成功")
                return True
            else:
                print("[verify_permission] 程序自检失败，没有权限启动")
                return False
                
        except:
            print("[verify_permission] 程序自检失败，请检查您的计算机环境")
            return False

        
