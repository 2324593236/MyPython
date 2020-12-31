#实例四：模拟银行
card1="111"
pwd1="123456"
ban1=10000

card2="222"
pwd2="123456"
ban1=10000

card3="333"
pwd3="123456"
ban1=10000

times=1

while True:
    print("欢迎来到模拟银行！")
    card=input("请输入银行卡号：")
    pwd=input("请输入银行密码：")

    ban=0

    if card==card1 and pwd==pwd1:
        ban=ban1

    elif card==card2 and pwd==pwd2:
        ban=ban2

    elif card==card3 and pwd==pwd3:
        ban=ban3

    else:
        times=times+1
        if times>=3:
            print("您已输入错误三次,请联系后台")
            break
        elif times<3:
            print("您已输入错误",times,"次,三次输入错误后，请联系后台取卡")
            continue

    while True:
        num=input("请输入您要办理的业务(1.存款 2.取款 3.退卡):")
        if num=="1":
           inn=float(input("请输入存款金额："))
           if inn<=0:
               print("存款金额请大于零")
               continue
           elif inn>0:
                ban=ban+inn
                print("存入:",inn,"余额:",ban)

        elif num=="2":
            out=float(input("请输入取款金额："))
            if out<0:
                print("取款金额不能小于0")
            elif out>ban:
                print("取款金额不能大于余额")
            else:
                ban=ban-out
                print("取出:",out,"余额:",ban)
                print("取款完成,注意退卡")
            continue
        elif num=="3":
            print("请取走卡片,欢迎下次再来")

        else:
            print("您输入有误！")
            continue
