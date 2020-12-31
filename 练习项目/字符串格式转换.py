str = input('输入要转换的字符串：')
# str = '\u8bb8\u6d77\u6960'#许海楠
# str = '\u502a\u656c\u5e05'#倪敬帅
# str = 'u7231'#爱
# str = e8ae b8e6 b5b7 e6a5 a0#十六进制
str1 = str.encode('utf-8')
print("UTF-8编码格式：%s" % str1)
str2 = str.encode('utf-16')
print("UTF-16编码格式：%s" % str2)
str3 = str.encode('gbk')
print("GBK编码格式：%s" % str3)
str4 = str.encode('unicode_escape')
print("Unicode编码格式：%s" % str4)