import socket

class verify():

    def __init__(self):
        #self.data = {}
        self.host = "0.0.0.0"
        self.port = 2333
        self.receive_data = None
        self.send_data = None
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.host, self.port))
    
    def listen(self):
        # 设置最大连接数，超过后排队
        self.socket.listen(5)

        while True:
            # 建立客户端连接
            clientsocket, addr = serversocket.accept()

            print("连接地址: " + str(addr))

            msg = clientsocket.recv(1024).decode()
            print(msg)
            if msg == "ASDAN_normal":
                print("允许运行")
                clientsocket.send("TRUE".encode('utf-8'))
            else:
                print("拒绝运行")
                clientsocket.send("FALSE".encode('utf-8'))

            clientsocket.close()

    def request_cmd(self):

        