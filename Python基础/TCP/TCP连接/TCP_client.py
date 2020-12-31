###TCP
##创建TCP客户端
import socket#调用socket套接字模块
host = socket.gethostname()#获取地址IP设置为主机IP地址,
port = 12345#设置端口号(须大于1024)
tcp_client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)#创建套接字,使用IPV4，TCP协议
tcp_client.connect((host,port))#连接服务器
print("服务器已连接")
values = ""#初始化变量
while values != "关闭连接":#判断数据是否为 关闭连接
    send_values = input("输入要发送的数据：")#输入要发送的数据
    tcp_client.send(send_values.encode())#发送数据，须将数据转换为字节类型
    if send_values == "关闭连接":#如果接收的数据不为 关闭连接时
        break#跳出循环
    values = tcp_client.recv(1024).decode()#接收数据(接收最大字节1024),须将字节类型数据转换为字符串类型数据
    print("接收的数据：%s" % values)#输出服务器返回数据
tcp_client.close()#关闭客户端
