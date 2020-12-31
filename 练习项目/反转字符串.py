##反转字符串
while True:
    str1 = input("请输入要反转的字符串：")
    list1 = reversed(str1)
    list1 = list(list1)
    str2 = ''.join(list1)
    print("输入的字符串",str1)
    print("反转后的字符串："+str2+"\n")
