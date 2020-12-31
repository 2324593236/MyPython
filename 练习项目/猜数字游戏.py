#项目名称：猜数字游戏
#项目功能：
#用户输入一个数字
import random
answer = random.randint(1,10)
counts = 0
while counts <3:
    num = int(input("请输入我心里想的数字:"))
#判断用户输入数字大小
#数字大了的话提示大了
#数字小了的话提示小了
#数字对了的话提示对了
    if num == answer:
        print("妈的，猜对了！！！")
        break;
    elif num < 6:
        print("看，小了吧！！！")
    elif num > 6:
        print("看，大了吧！！！")
    counts = counts + 1
    if counts == 3:
        print("算了吧你，跟个弱智一样")
print("算你过关")
