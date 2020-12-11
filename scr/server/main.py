
# 导入 socket、sys 模块
import socket

# 创建 socket 对象
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定端口号
serversocket.bind(("127.0.0.1", 2333))

# 设置最大连接数，超过后排队
serversocket.listen(5)

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