##函数

##函数的创建定义
def function1(parameter1='value1',parameter2='value2'):#定义一个函数functionname=function1，函数的关键参数parametername=parameter1,parameter2，参数的默认值为value1，value2
    """comments       #函数
       测试定义        #的
    """              #注释
    parameter1 += parameter1 #定义函数functionname的参数parametername的功能
    print(parameter1)

parameter2 = [123]
def function2(parameter2):#定义个空函数
    pass

##函数的调用
function1(parameter2)
print(parameter2)
##函数的参数
#print(function1.__defaults__)#用functionname.__defaults__方法查询函数的参数默认值
#def function3(*parameter3="list1")#一个"*"的可变参数，parameter3对应列表，位置
#    pass
#
#def function4(**parameter4="dictionary2")#两个"*"的可变参数，parameter4对应字典，关键字
#    pass

##函数的返回值return
#return item1#返回一个元素时，返回的值可以是任意类型
#return item1,item2#返回多个元素时，返回的值是元组

##函数的变量
i1 = "None"#定义一个全局变量i1
def function5():
    global i2 #用global方法将局部变量改为全局变量
    i2 = 'None'#定义一个函数的局部变量i2
    print(i1)
    print(i2)
function5()
print(i1)#局部变量不能直接输出
print(i2)#全局变量可以直接输出

##匿名函数
function6 = lambda parameter5:parameter5 + parameter5#通过functionname = lambda parametername:parametername方法创建一个匿名函数
print(function6("value"))