###UDP
##创建UDP客户端
import socket#调用socket套接字模块
host = "127.0.0.1"#设置主机IP地址
port = 8080#设置端口号
while True:
    udp_client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)#创建套接字
    send_values = input("输入要发送的数据：")#输入要发送的数据
    udp_client.sendto(send_values.encode(),(host,port))#发送字节类型数据到(host,port)
    print("发送的数据：%s" % udp_client.recv(1024).decode())#接收数据并转换为字符串类型
    udp_client.close()#关闭客户端

