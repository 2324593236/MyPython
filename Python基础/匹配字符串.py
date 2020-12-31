#re正则表达式模块
import re
#匹配字符串
##re.match(pattern,string,[flags]) pattern模式字符串，string匹配字符串，flags匹配方式 re.l不分大小写 re.A让\w不匹配汉字

mb = r'a\w'
str = 'asdaf Asdaf'
match = re.match(mb,str,re.I)
print(match)
