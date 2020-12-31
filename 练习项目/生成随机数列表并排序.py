#生成随机数列表并排序
 #sorted函数排序不会改变原列表元素顺序
 #sort方法排序会改变原列表元素的顺序
import random #调用随机数模块
list1=[random.randint(1,99) for n in range(20)]#随机生成20个1-99之间的数
##list1=[]
##while len(list1) < 20:#限制列表长度为20
##    number= random.randint(1,99)#生成1-99之间的随机数并赋值给变量number
##    list1.append(number)#将随机数添加至列表list1末尾
print("生成随机数列表为：",'\n',list1)
list2 = sorted(list1,key=None,reverse=False)#key=str.lower为不区分大小写,reverse=False为升序,reverse=True为降序
print("用sorted函数进行升序排序得：","\n",list2)
list3 = sorted(list1,key=None,reverse=True)
print("用sorted函数进行降序排序得：","\n",list3)

list1.sort(key=None,reverse=False)
print("用sort方法进行升序排序得：","\n",list1)
list1.sort(key=None,reverse=True)
print("用sort方法进行降序排序得：","\n",list1)
