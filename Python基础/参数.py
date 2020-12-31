#参数的传递
def show(name,age,sex,habby):
    print("我叫：",name,"年龄：",age,"性别：",sex,"爱好：",habby)

show ("张三","99","男","玩")#顺序传入
show (name="张三",age="99",sex="男",habby="玩")#关键词传入

#不定长参数
def add(*args):
    summ=0
    for i in args:
        summ=summ+i
    return summ
    
a=add(int(input("输入一个数")),
      int(input("输入一个数")),
      int(input("输入一个数")))
print(a)

