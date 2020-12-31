###文件
import os#调用os模块
##文件的创建与打开
#file = open(filename[,mode[,buffering]])#用open()函数打开文件，filename为文件名，mode为读取方式，buffering缓存模式
###mode打开方式
##r为只读模式打开文件，文件指针放在文件的开头
##rb为以二进制格式打开文件，并采用只读模式，文件的指针将会放在文件的开头，一般用于非文本文件，
##r+为可以读取文件，也可以写入新的内容覆盖原有内容（从文件开头进行覆盖）
##rb+为以二进制格式打开文件，并采用读写模式，文件的指针将会放在文件的开头，一般用于非文本文件
##w为以只写模式打开文件
##wb为以二进制格式打开文件，并采用只写模式，一般用于非文本文件
##w+为打开文件后先清空原有内容，对这个空文件有读写权限
##wb+以二进制格式打开文件并采用读写模式，一般用于非文本文件
##a为已追加模式打开文件，如果该文件已经存在，文件指针将放在文件末尾，否则创建新文件用于写入
##ab为以二进制格式打开文件，并采用追加模式，如果该文件已经存在，文件指针将放在文件末尾，否则创建新文件用于写入
##a+为以读写模式打开文件，如果该文件已经存在，文件指针将放在文件末尾，否则创建新文件用于读写
##ab+为以二进制格式打开文件，并采用追加模式，如果该文件已经存在，文件指针将放在文件的末尾，否则创建新文件用于读写
###buffering缓存模式
##为0时不缓存
##为1时缓存
##大于1时缓冲区大小
file1 = open("测试(None).txt","a+",)#打开文件,追加
file1.write("jadlgjdsgjlk\n")#文件的写入
file1.close()#文件的关闭
print(file1.closed)#文件的关闭状态，True为关闭，Flase为打开
with open('测试(None).txt','r+') as file1:#用with open(filename[,mode[,buffering]]) as file 方式打开文件，文件会在执行后自动关闭
    value1 = file1.read()#文件的读取
    print("读取全部",value1)
    value2 = file1.readline()#读取一行
    print("读取一行",value2)
    value3 = file1.readlines()#读取全部，返回字符串列表
    print("读取全部：",value3)
    file1.flush()#写入当前缓冲区内容
print(file1.closed)

##删除文件
#os.remove(path)
if os.path.exists(r"E:\Python\Python学习\测试(None).txt"):#判断文件是否存在
    os.remove(r"E:\Python\Python学习\测试(None).txt")#存在的话，删除文件
else:
    print("文件不存在")
with open(r"E:\Python\Python学习\测试(None).txt","a+") as file2:#无意义，还原操作
    pass

##重命名文件
#os.rename(oldname,newname)#os.rename()重命名函数,oldname为被重命名的目录路径或文件名，newname为命名后的目录路径或文件名
if os.path.exists(r"E:\Python\Python学习\测试(None).txt"):#判断文件是否存在
    try:
        os.rename(r"E:\Python\Python学习\测试(None).txt",r"E:\Python\Python学习\测试1(None).txt")#用os.rename()函数修改文件名
    except FileExistsError:
        print("文件名重复")
else:
    print("文件不存在")
##获取文件的基本信息
#os.stat(path)#获取文件基本信息，返回值是一个对象
def formattime(longtime):#创建格式化时间的函数
    import time#调用time时间模块
    return time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(longtime))#用time.strftime()函数格式化时间%Y年-%m月-%d日 %H时-%M分-%S秒，time.localtime()转换成本地时间
def formatbyte(number):#创建格式化文件大小的函数
    for (value4,item1) in [(1024,"KB"),(1024*1024,"MB"),(1024*1024*1024,"GB")]:#定义多少字节是为什么单位
        if number >= value4:#当字节数大于某段字节时
            return "%.2f %s" % (number*1.0/value4,item1)#格式化要输出的字符串
        elif number == 1:
            return "1 字节"
        else:
            byte = "%.2f" % (number or 0)#当大小小于一个字节时，将number格式化成小数点后两位的浮点型
            return (byte[:-3] if byte.endswith(".00") else byte) + "字节"#从byte倒数第三个数字开始，如果不是.00结尾的话，输出byte,
    
file2 = os.stat(r"E:\Python\Python学习\测试(None).txt")
print("文件完整路径:",os.path.abspath(r"E:\Python\Python学习\测试(None).txt"))#获取文件完整路径
print("索引号：",file2.st_ino)#文件索引号
print("设备名：",file2.st_dev)#文件设备名
print("文件大小：",formatbyte(file2.st_size))#文件大小
print("最后访问时间：",formattime(file2.st_atime))#文件最后访问时间
print("最后修改时间：",formattime(file2.st_mtime))#文件最后修改时间
print("最后改变时间：",formattime(file2.st_ctime))#文件最后改变时间

