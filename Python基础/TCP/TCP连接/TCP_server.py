###TCP
##创建TCP服务器
import socket#调用socket套接字模块
host = socket.gethostname()#获取地址IP设置为主机IP地址,
port = 12345#设置端口号(须大于1024)
tcp_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)#创建套接字,使用IPV4，TCP协议
tcp_server.bind((host,port))#绑定IP地址和端口号，元组类型参数
tcp_server.listen(1)#监听，最大监听数量1
sock,addr = tcp_server.accept()#等待接收，sock新的socket对象，addr连接客户端的IP地址
print("服务器已连接")
values = sock.recv(1024).decode()#创建客户端接收对象，指定最大接收数量1024
while values != "关闭连接":#如果接收的数据不为 关闭连接时
    if values:#如果接收的数据不为空
        print("接收的数据：%s" % values)#输出接收数据
    send_values = input("输入要发送的数据：")#输入要发送的数据
    sock.send(send_values.encode())#向客户端发送字节类型数据
    if send_values == "关闭连接":#如果接收的数据不为 关闭连接时
        break#跳出循环
    values = sock.recv(1024).decode()#接收数据（最大1024字节），并装换为字符串类型
sock.close()#关闭连接
tcp_server.close()#关闭服务器
