###用Process创建2个子进程，并记录运行时间
from multiprocessing import Process#调用multiprocessing进程模块
import time#调用时间模块
import os

##方法一
##def test1(intervel):#创建子进程函数
##    print("子进程%s开始执行,他的父进程是%s" %(os.getpid(),os.getppid()))#获取进程ID，获取父进程ID
##    t_start = time.time()#记录子进程开始时间
##    time.sleep(intervel)#用time.sleep()间隔时间
##    t_end = time.time()#记录子进程结束时间
##    print("子进程%s 执行时间为%0.2f秒" %(os.getpid(),t_end-t_start))#获取进程ID,计算进程运行时间
##
##def test2(intervel):#创建子进程函数
##    print("子进程%s开始执行,他的父进程是%s" %(os.getpid(),os.getppid()))#获取进程ID，获取父进程ID
##    t_start = time.time()#记录子进程开始时间
##    time.sleep(intervel)#用time.sleep()间隔时间
##    t_end = time.time()#记录子进程结束时间
##    print("子进程%s 执行时间为%0.2f秒" %(os.getpid(),t_end-t_start))#获取进程ID,计算进程运行时间
##
##def main():#创建主进程函数
##    print("主进程开始")
##    print("主进程的PID:%s" % os.getpid())#获取进程ID
##    p1 = Process(target=test1,name="p1",args=(1,))#调用Process类创建子进程test1,传递元组(1,)参数
##    p2 = Process(target=test2,name="p2",args=(2,))#调用Process类创建子进程test2,传递元组(2,)参数
##    p1.start()#调用.start()方法执行进程p1
##    p2.start()#调用.start()方法执行进程p2
##    print("p1.is_alive=%s" % p1.is_alive())#用.is_alive()方法判断进程p1是否正在运行
##    print("p2.is_alive=%s" % p2.is_alive())#用.is_alive()方法判断进程p2是否正在运行
##    print("p1.name=%s" % p1.name)#用.name方法获取进程p1名字
##    print("p1.id=%s" % p1.pid)#用.pid方法获取进程p1的ID
##    print("p2.name=%s" % p2.name)#用.name方法获取进程p2名字
##    print("p2.id=%s" % p2.pid)#用.pid方法获取进程p1的ID
##    p1.join()#主进程等待子进程p1运行结束
##    p2.join()#主进程等待子进程p2运行结束
##    print("主进程结束")
##if __name__ == "__main__":#建立主程序
##    main()#执行main函数

#方法二
class SubProcess(Process):#定义一个类，继承模块multiprocessing中Process类
    def __init__(self,interval,name=''):#定义一个初始化方法
        super(SubProcess,self).__init__()#继承父类的初始化方法
        #Process.__init__(self)#继承父类的初始化方法
        self.interval = interval#初始化传递的interval值
        if name:#判断name是否存在
            self.name = name#初始化传递的name值
    def run(self):#定义一个函数
        print("子进程%s开始执行,他的父进程是%s" %(os.getpid(),os.getppid()))#获取进程的ID，获取父进程的ID
        t_start = time.time()#记录进程开始执行时间
        time.sleep(self.interval)#用time.sleep()间隔时间
        t_end = time.time()#记录进程结束时间
        print("子进程%s 执行时间为%0.2f秒" %(os.getpid(),t_end-t_start))#获取进程的ID值，计算进程运行时间
        
def main():#创建主进程函数
    print("主进程开始")
    print("主进程的PID:%s" % os.getpid())#获取进程ID
    p1 = SubProcess(interval=1,name="p1")#调用SubProcess类创建子进程,传递参数interval=1,name="p1"
    p2 = SubProcess(interval=2,name="p2")#调用SubProcess类创建子进程,传递参数interval=2,name="p2"
    p1.start()#调用.start()方法执行进程p1
    p2.start()#调用.start()方法执行进程p2
    print("p1.is_alive=%s" % p1.is_alive())#用.is_alive()方法判断进程p1是否正在运行
    print("p2.is_alive=%s" % p2.is_alive())#用.is_alive()方法判断进程p2是否正在运行
    print("p1.name=%s" % p1.name)#用.name方法获取进程p1名字
    print("p1.id=%s" % p1.pid)#用.pid方法获取进程p1的ID
    print("p2.name=%s" % p2.name)#用.name方法获取进程p2名字
    print("p2.id=%s" % p2.pid)#用.pid方法获取进程p1的ID
    p1.join()#主进程等待子进程p1运行结束
    p2.join()#主进程等待子进程p2运行结束
    print("主进程结束")
if __name__ == "__main__":#建立主程序
    main()#执行main函数
