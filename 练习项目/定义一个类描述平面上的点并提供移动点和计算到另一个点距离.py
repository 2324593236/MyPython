from math import sqrt
class Point(object):
    def __init__ (self,x=0,y=0):#原点坐标
        self.x = x
        self.y = y
    def move_to(self,x,y):#移动点的坐标
        self.x = x
        self.y = y
    def move_by(self,x_by,y_by):#点位移的量
        self.x += x_by
        self.y += y_by
    def long(self,other):#计算原点和另一个点的距离
        x_by = self.x - other.x
        y_by = self.y - other.y
        return sqrt(x_by ** 2 + y_by ** 2)
    def __str__(self):
        return "(%s,%s)" % (str(self.x),str(self.y))
def main():#主程序运行函数
    p1 = Point(3,5)
    p2 = Point()
    print(p1)
    print(p2)
    p2.move_by(-1,2)
    print(p2)
    print(p1.long(p2))
if __name__ == '__main__':
    main()