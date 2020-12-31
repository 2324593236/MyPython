#花鼓骰
from random import randint as sj
a,b = None,None
money = 1000
while money>0:
    print("余额：",money)
    start1 = input("请下注：")
    if start1:
        start1 = int(start1)
    else :
        continue
    if start1>money:
        print("余额不足，请重新下注")
        continue
    while True:
        a = sj(1,6)+sj(1,6)
        if a==7 or a==11:
            print("玩家赢，奖励%d，余额%d"%(start1*2,money+(start1)*2))
            money+=(start1*2)
            break
        elif a==2 or a==3 or a==12:
            print("庄家赢，扣除%d，余额%d"%(start1,money-start1))
            money = money-start1
            break
        else:
            continue
if money<=0:
    print("游戏结束")