#分别向队列中写入和读取数据
from multiprocessing import Process,Queue
import time

def write(q):
    if not q.full():#判断队列是否满
        for i in range(5):
            message = "数据"+str(i)
            q.put(message)
            time.sleep(0.2)
            print("写入：%s" % message)

def read(q):
    if not q.empty():#判断队列是否为空
        for i in range(5):
            time.sleep(0.2)
            print("读取：%s" % q.get_nowait())
if __name__ == "__main__":
    print("主进程开始")
    q = Queue()
    pw = Process(target=write,args=(q,))
    pr = Process(target=read,args=(q,))
    pw.start()
    pr.start()
    pw.join()
    pr.join()
    print("主进程结束")
