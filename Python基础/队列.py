###队列Queue
##Queue.put(item[,block[,timeout]]):将item数据插入队列，block默认值为True
##Queue.put_nowait(item):相当于Queue.put(item,False)
##Queue.get([block[,timeout]]):获取队列数据然后从队列移除，block默认值为True
##Queue.get_nowait():相当于Queue.get(False)
##Queue.empty():判断队列是否为空，空为True,否则为False
##Queue.full():判断队列是否已满，满为True,否则为False
##Queue.qusize():返回当前队列所含数据数量

#进程中的队列
##from multiprocessing import Queue#调用multiprocessing模块中Queue类
##if __name__ == "__main__":#创建主程序
##    q = Queue(3)#建立队列容量3
##    q.put("数据1")#插入数据
##    print("队列是否已满：%s" % q.full())#判断数列是否已满
##    q.put("数据2")#插入数据
##    q.put("数据3")#插入数据
##    print("队列是否已满：%s" % q.full())#判断数列是否已满
##
##    try:#测试语句
##        q.put("数据4",block=True,timeout=2)#插入数据，是否定义处理时间True,处理时间为2秒
##    except:#异常反馈
##        print("满了,队列现有%s条数据" % q.qsize())
##    if not q.empty():#队列不为空时
##        print("获取数据")
##        for i in range(q.qsize()):#执行数据条数次
##            print(q.get_nowait())#从队列取出数据，无需等待

#线程中的队列
from queue import Queue#调用queue队列模块中的Queue类
from threading import Thread#调用threading线程模块中的Thread类
import time#调用时间模块
import random#调用随机数模块
class Producer(Thread):#建立一个子类继承threading线程模块中的Thread类
    def __init__(self,name,queue):#定义一个初始化方法
        Thread.__init__(self,name=name)#继承父类的初始化方法
        self.data = queue#初始化传递的参数
    def run(self):#定义一个run()函数
        for i in range(5):#执行5次
            print("%s将%d加入队列" % (self.getName(),i))#获取线程的别名
            self.data.put(i)#取出队列中的数据
            time.sleep(random.random())#延迟随机时长
        print("%s完成" % (self.getName()))#获取线程别名
class Consumer(Thread):#建立一个子类继承threading线程模块中的Thread类
    def __init__(self,name,queue):#定义一个初始化方法
        Thread.__init__(self,name=name)#继承父类的初始化方法
        self.data = queue#初始化传递的参数
    def run(self):#定义一个run()函数
        for i in range(5):#执行5次
            val = self.data.get()#数据存入队列
            print("%s将%d取出队列" % (self.getName(),val))#获取线程的别名
            time.sleep(random.random())#延迟随机时长
        print("%s完成" % (self.getName()))#获取线程的别名
        
if __name__ == "__main__":#创建主程序
    print("主线程开始")
    queue = Queue()#定义一个队列
    producer = Producer("Producer",queue)#执行Thread子类
    consumer = Consumer("Consumer",queue)#执行Thread子类
    producer.start()#线程开始执行
    consumer.start()#线程开始执行
    producer.join()#等待线程执行结束
    consumer.join()#等待线程执行结束
    print("主线程结束")
