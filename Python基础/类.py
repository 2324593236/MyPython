##类

#类的与定义创建
class Class1:#定义一个类
    """测试"""#类的帮助信息
    pass#类体，类的方法属性
Class1#调用类

#类的实例、实例方法的创建和访问
class Class2():
    def function1(self,state1,state2="实例方法2"):#用def functionname(self,statename1,statename2=value1):方法创建类的实例方法，functionname是方法名，statename是功能名,功能可附默认值
        print(state1)
        print(state2)
template1 = Class2()#创建实例
print(template1)#访问实例
template1.function1("实例方法1")#访问实例方法

#__init__方法创建类的方法
class Class3:
    def __init__(self,parameter1,parameter2="构造方法2"):#用__init__(self,parametername1,patametername2=value1)定义构造方法,一个类里只能存在一个init构造方法，self不可省略,可以构造多个方法，方法可附默认值
        print("这是构造方法：")
        print(parameter1)
        print(parameter2)
index1 = "构造方法1"
Class3(index1)#调用类,

#类的类属性的创建和访问
class Class4():
    pattern1 = "类属性1"#定义一个类属性
    pattern2 = 0#定义一个类属性2=0，类属性的值在所有实例之间共用
    def __init__(self):  # 用__init__(self)定义构造方法,一个类里只能存在一个init构造方法，self不可省略,可以构造多个方法，方法可附默认值
        Class4.pattern2 += 1 #类属性2的值加1
        print("第%d个类属性"%Class4.pattern2)#在构造方法中访问类属性
        print(Class4.pattern1)#类属性的访问Classname.patternname,类名.属性名
list1 = []
for i in range(3):
    list1.append(Class4())#创建类的实例
print("共%d个类属性"%Class4.pattern2)
Class4.pattern3 = "类属性3"#添加类属性3
print(list1[1].pattern3)#访问列表中第2个类的类属性3

#类的实例属性的创建与访问
class Class5():
    def __init__(self):
        self.pattern4 = "实例属性1"#定义一个实例属性
        print(self.pattern4)#访问实例属性
template2 = Class5()#实例化类的对象
template3 = Class5()
print(template2.pattern4)#通过templatename.leg方法访问实例属性，templatename类的对象名，实例属性只能通过类的对象进行访问，不能通过类名直接访问
template3.pattern4 = "修改的实例属性"#实例属性可以访问对象进行赋值修改，并不影响其他实例属性
print(template3.pattern4)

#访问限制
class Class6():
    _pattern5 = "保护类型的属性"#_patternname定义一个保护类型的属性,_+patternname属性名
    def __init__(self):
        print(Class6._pattern5)#访问保护类型的属性
template4 = Class6()#创建类的实例对象
print(template4._pattern5)#保护类型的属性可以通过实例对象名进行访问
print(Class6._pattern5)#保护类型属性可以通过类名进行访问

class Class7():
    __pattern7 = "私有类型的属性"  # __patternname定义一个私有类型的属性,__+patternname属性名
    def __init__(self):
        print(Class7.__pattern7)#访问私有类型的属性
    def function2(self):
        print(Class7.__pattern7)#访问私有类型属性
template5 = Class7()#创建类的实例对象
print(template5._Class7__pattern7)#私有类型的属性可以通过实例对象名templatename._Classname__patternname进行访问
template5._Class7__pattern7 = "修改的私有类型属性"#修改私有类型属性的值，不能在类的方法执行中修改
template5.function2()#方法执行中的私有属性的值
print(template5._Class7__pattern7)#直接访问私有属性的值

#类的计算属性@property
class Class8():
    def __init__(self,x,y):
        self.x = x
        self.y = y
    @property#装饰器，将方法转化为属性，可以通过方法名使用方法不用添加小括号，不能进行赋值
    def function3(self):
        return self.x*self.y
template6 = Class8(1,2)#创建类的实例对象
print(template6.function3)#访问实例对象的方法

#类的属性添加保护机制_保护类型——>__私有类型
class Class9():
    def __init__(self,parameter3):
        self.__parameter3 = parameter3#赋值私有类型属性
    @property#装饰器
    def function4(self):
        return self.__parameter3#返回私有类型属性
template7 = Class9("添加保护机制")
print(template7.function4)

#类的继承
class Class10():#创建一个基类
    pattern8 = "value2"#定义一个类属性
    def function5(self,pattern8):
        print(pattern8)
        print(Class10.pattern8)
class Class11(Class10):#创建一个子类继承基类的方法
    pattern8 = "value3"
    def __init__(self):
        print("value4")
class Class12(Class10):
    pattern8 = "value5"
    def __init__(self):
        print("value6")
template8 = Class11()
template8.function5(template8.pattern8)
template9 = Class12()
template9.function5(template9.pattern8)
template10 = Class10()
print(template10)
template10.function5("value7")