###TCP
##创建TCP服务器
import socket#调用socket套接字模块
host = "127.0.0.1"#设置主机IP地址
port = 8080#设置端口号
tcp_server = socket.socket()#创建套接字
tcp_server.bind((host,port))#绑定IP地址和端口号，元组类型参数
tcp_server.listen(5)#监听，最大监听数量5
print("服务器等待连接")
while True:#死循环
    conn,addr = tcp_server.accept()#等待接收，conn另一个socket对象，addr连接客户端的IP地址
    data = conn.recv(1024)#创建客户端接收对象，指定最大接收数量1024
    print(data)#输出接收数据
    conn.sendall(b"HTTP/1.1 200 OK\r\n\r\nHello World")#向客户端发送字节类型数据
    conn.close()#关闭客户端
