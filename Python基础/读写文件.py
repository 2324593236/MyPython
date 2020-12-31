#文件的写入
text='This is my first test.\nThis is my next line.\nThis is my last line.'

my_file=open('my write file.txt','w')#用写入形式打开
my_file.write(text)#写入
my_file.close()#关闭

append_text='\nThis is appended file'
my_file=open('my write file.txt','a')#用添加形式打开
my_file.write(append_text)#写入
my_file.close()#关闭

file=open('my write file.txt','r')#用只读形式打开
#content1=file.read()#读取
#print(content1,'\n')
content2=file.readline()#一行读取
print(content2,'\n')
content3=file.readlines()#足行读取
print(content3,'\n')
