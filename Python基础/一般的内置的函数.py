#函数

#函数的调用
def add(a,b,c,d):#定义一个函数add,变量a,b,c,d
    e=a+b+c+d#赋予函数功能
    return e

result=add(1,2,3,4)
print(result)
print(add(1,2,3,4))

#榨汁机小测试
def zzj(x):
    if x=="苹果" or x=="桃子" or x=="橙子":
        print("正在榨汁")
        print("two minutes")
        zhi="一杯"+x+"汁"
        return zhi
    else :
        print("炸不了")

guozhi=zzj(input("你要榨什么："))
print(guozhi)
    

#内置函数
*max()#最大值函数
*min()#最小值函数
round(x,2)#保留到小数点后两位函数
*print()#打印输出函数
*input()#输入函数
*int()#转整型
*float()#转浮点型
*str()#转字符串
set()#转为空集合
hex()#整数转十六进制字符串
oct()#整数转八进制字符串
*len()#计算长度
*list()#序列转列表
*sum()#序列元素和
sorted()#序列元素排序，由小到大，由a到z
reversed()#反转序列元素，返回非序列
enumerate()#为序列元素添加索引值，返回非序列
*range()#生成元素
zip()#特殊函数
tuple()#转换成元组
dict()#转换成字典
connect()#连接函数，生成连接对象
.count()#获取指定元素出现次数
.index()#获取函数索引
soted(listname,key=None,reverse=False)#对列表元素的升降排列：key=str.lower为不区分大小写,reverse=False为升序,reverse=True为降序
strname.strip([chars])#去除字符串左右两边的字符,chars为用来去除的字符
strname.lstrip([chars])#去除字符串左边的字符,chars为用来去除的字符
strname.rstrip([chars])#去除字符串右边的字符,chars为用来去除的字符


#方法
listname.append(item)#在列表末尾添加元素
listname.insert(index,item)#在列表任意位置添加元素
listname.extend()#在列表后面添加列表
listname.remove()#删除列表中元素
lisname.sort(key=None,reverse=False)#列表元素的升降排序：key=str.lower为不区分大小写,reverse=False为升序,reverse=True为降序
strname.encode()#转换为UTF-8编码
strname.encode('gbk')#转换为GBK编码
strname.split(sep,num)#分割方法，sep为以什么作为分隔符，num为分割次数，为-1时不限次数
strname.join(listname)#连接方法
strname.count(sub[,start[,end]])#检索一个字符串在另一个字符串中出现次数的,sub检索的字符串,检索起始位置,检索结尾位置
strname.find(sub[,start[,end]])#检索一个字符串在另一个字符串内首次出现的位置,sub检索的字符串,检索起始位置,检索结尾位置
strname.rfind(sub[,start[,end]])#检索一个字符串在另一个字符串内最后出现的位置,sub检索的字符串,检索起始位置,检索结尾位置
strname.index(sub[,start[,end]])#检索一个字符串在另一个字符串内首次出现的位置,sub检索的字符串,检索起始位置,检索结尾位置
strname.rindex(sub[,start[,end]])#检索一个字符串在另一个字符串内最后出现的位置,sub检索的字符串,检索起始位置,检索结尾位置
strname.startswich(sub[,start[,end]])#检索是否以指定字符串开头,sub检索的字符串,检索起始位置,检索结尾位置
strname.endswich(sub[,start[,end]])#检索是否以指定字符串结尾,sub检索的字符串,检索起始位置,检索结尾位置
strname.lower()#转换为小写
strname.upper()#转换为大写
'%[-][+][0][m][.n]'格式化字符'%exp  #[-]左对齐,正数前没符号,负数前加- [+]右对齐,正数前加+,负数前加- [0]右对齐,正数前没符号,负数前加-,用0填充空白处 [m]所占宽度 [.n]小数点后保留n位数 格式化字符表示格式化成的类型 exp要转换的项
strname.format(args) #格式化字符串, strname为模板,{[index][:[[fill]align][sign][#][width][.precision][type]]} index索引值，fill空白处填充字符，align对齐方式<左对齐 >右对齐 =内容左对齐并把符号放在填充内容最右侧 ^内容居中，sign有无符号数
dict.fromkeys(keyname)#创建有键的字典
dictionaryname.get(keyname,[default])#访问字典中keyname键的值，default为访问键不存在时返回的值
dictionaryname.keys()#访问字典的键
dictionaryname.values()#访问字典的值
setname.add()#集合添加元素
setname.remove(valuename)#集合移除元素valuename
setname.pop()#随机移除集合内的一个元素，并返回所移除的元素
setname.clear()#清空集合内元素
