##字符串
import re#调用re正则表达式
str1 = "1213141516171"#直接定义字符串
str2 = "AfaAgsAhAjAe"
str3 = " \n\t\ra12你是的\n\t\r a"
str4 = str(23456)#用str()函数将数据类型转换为字符串

#字符串的拼接
str4 = str1 + str2#用+连接字符串
print(str4)

#字符串的长度
print(len(str3))#用len()函数进行查看字符串长度
print(len(str3.encode()))#strname.encode()函数转换为UTF-8编码
print(len(str3.encode("gbk")))#strname.encode("gbk")函数转换为GBK编码

#字符串截取
print(str4[1:6:1])#截取索引值1-5的字符，步长为1

#字符串分割
print(str1.split("1",2))#用strname.split(item,count)方法进行1为分隔符分割2次

patter1 = r"[a|b]"#定义分割符a或者b
split1 = re.split(patter1,str2,3,re.I)#re.split(patternname,strname,count,flags)方法，以patternname为分隔符，分割字符串strname，分割count次，flags为re.I不区分大小写
print(split1)

#字符串合并
print("@".join(str1))#用item.join(strname)方法进行@为连接符的元素连接

#字符串检索
print(str1.count("1",0,9))#用strname.count(item[,start[,end]])方法检索字符串中索引0-9之间存在字符1的次数
print(str1.find("1",0,9))#用strname.find(item[,start[,end]])方法检索字符串中索引0-9之间字符1首次出现的索引位置
print(str1.rfind("1",0,9))#用strname.rfind(item[,start[,end]])方法检索字符串中索引0-9之间字符1最后出现的索引位置
print(str1.index("1",0,9))#用strname.index(item[,start[,end]])方法检索字符串中索引0-9之间字符1首次出现的索引位置,不存在是返回异常
print(str1.rindex("1",0,9))#用strname.rindex(item[,start[,end]])方法检索字符串中索引0-9之间字符1最后出现的索引位置,不存在是返回异常
print(str1.startswith("1",0,9))#用strname.startswich(item)方法检索字符串中索引0-9之间的字符是否以字符1为开头
print(str1.endswith("1",0,9))#用strname.endswich(item)方法检索字符串中索引0-9之间的字符是否以字符1为结尾

#字符串的转换
print(str2.lower())#用strname.lower()方法使字符串中的大写字母全部转换为小写
print(str2.upper())#用strname.upper()方法使字符串中的小写字母全部转换为大写

#字符串中空格与特殊字符的去除
print(str3.strip())#用strname.strip()方法去除首尾的特殊字符
print(str3.strip("a"))#用strname.strip(item)方法去除首尾的指定字符
print(str3.lstrip("a"))#用strname.lstrip(item)方法去除左侧的指定字符
print(str3.rstrip("a"))#用strname.strip(item)方法去除右侧的指定字符

#字符串的格式化
#"%[-][+][0][m][.n]格式化字符"%item
template1 = "姓名： %s\t编号： %03d \t简介：%s"
tuple1 = ("倪",99,"adff")
print(template1%tuple1)

template2 = "姓名：{:s} \t编号：{:0>3s} \t简介：{:s}"
print(template2.format("倪","99","asd"))

##字符串的匹配
template3 = r"a"#模式字符串
match1 = re.match(template3,str2,re.I)#用re.match(templatename,strname,[flags])方法re.I不区分大小写匹配初次出现字符串，template为要匹配的模式字符串，strname被匹配的字符串，flags为匹配的模式
print(match1)
print(match1.start())#用re.matchname.start()方法查询匹配字符串首次出现的索引
print(match1.end())#用re.matchname.end()方法查询匹配字符串最后出现的索引
print(match1.group())#用re.matchname.group()方法查询匹配的字符串
search2 = re.search(template3,str3,re.I)#用re.search(templatename,strname,[flags])方法re.I不区分大小写匹配任意字符串，template为要匹配的模式字符串，strname被匹配的字符串，flags为匹配的模式
print(search2)
print(search2.start())#用re.searchname.start()方法查询匹配字符串首次出现的索引
print(search2.end())#用re.searchname.end()方法查询匹配字符串最后出现的索引
print(search2.group())#用re.matchname.group()方法查询匹配的字符串
findall1 = re.findall(template3,str3,re.I)#用re.findall(templatename,strname,[flags])方法re.I不区分大小写所有字符串并返回列表，template为要匹配的模式字符串，strname被匹配的字符串，flags为匹配的模式
print(findall1)

##字符串的替换
sub1 = re.sub(template3,"B",str2,9,re.I)#用re.sub(templatename,item,strname,count,flags)方法将字符串strname中的所有字符templatename替换为字符item，替换count次，re.I不区分大小写
print(sub1)