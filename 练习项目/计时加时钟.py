###计时器++时钟
import datetime
from time import sleep
import os
class Mytime(object):
    def __init__(self,h=0,m=0,s=0):#初始化变量
        self._h = h
        self._m = m
        self._s = s

    def run(self):#时间走字
        self._s += 1
        if self._s == 60:
            self._m += 1
            self._s = 0
            if self._m == 60:
                self._h += 1
                self._m = 0
                if self._h == 24:
                    self._h = 0

    def show(self):#时钟显示格式
        return "%02d:%02d:%02d" % (self._h,self._m,self._s)

def main():
    mytime =  Mytime(23,59,55)
    while True:
        print(mytime.show())
        print("现在时间为：%02d:%02d:%02d" % (datetime.datetime.now().time().hour,datetime.datetime.now().time().minute,datetime.datetime.now().time().second))
        sleep(1)
        os.system("cls")
        mytime.run()


if __name__ == "__main__":
    main()