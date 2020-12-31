###TCP
##创建TCP客户端
import socket#调用socket套接字模块
host = "127.0.0.1"#设置主机IP地址
port = 8080#设置端口号
while True:
    tcp_client = socket.socket()#创建套接字
    tcp_client.connect((host,port))#连接服务器IP地址和端口号，元组类型参数
    data1 = input("输入要发送的数据：")#接收数据
    tcp_client.send(data1.encode())#发送数据，须将数据转换为字节类型
    data2 = tcp_client.recv(1024).decode()#接收数据(接收最大字节1024),须将字节类型数据转换为字符串类型数据
    print("接收的数据为%s" % data2)#输出服务器返回数据
    tcp_client.close()#关闭客户端
