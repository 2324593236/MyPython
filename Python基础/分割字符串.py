import re
str='asadafagahajakawaeratay'
list=str.split('a')#以a为分隔符分割字符串str
list2=re.split(r'a',str)#以a为分隔符分割字符串str
for i in list:
    list1 = '       @'.join(list)#以@为分隔符连接列表list里的元素
print(list2)
print(list1)
