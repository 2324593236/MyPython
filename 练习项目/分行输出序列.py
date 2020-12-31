#项目名称：分行输出序列
list1 = ['a','b','c','d','e','f','g','h','i','g','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for number,index in enumerate(list1):
    if number%2 == 0:
        print(number,index,'\t\t\t\t',end='')# end='' 表示末尾加空格不换行
    else:
        print(number,index,'\n')
