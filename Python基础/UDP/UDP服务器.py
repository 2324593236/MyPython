###UDP
##创建UDP服务器
import socket#调用socket套接字模块
host = "127.0.0.1"#设置主机IP地址
port = 8080#设置端口号
while True:
    udp_server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)#创建套接字
    udp_server.bind((host,port))#绑定IP地址到端口号，元组类型参数
    print("绑定UDP到端口号8080")
    values,addr = udp_server.recvfrom(1024)#创建客户端接收对象，指定最大接收数量1024，返回值为元组，values为接收的数据对象，addr连接客户端的IP地址
    print("接收到的数据：%s" % values.decode())#输出接收数据,将字节类型数据转换为字符串类型
    send_values = values.decode()#将接收的数据转换为字节类型
    udp_server.sendto(send_values.encode(),addr)#向客户端发送字节类型数据
    udp_server.close()#关闭服务器
