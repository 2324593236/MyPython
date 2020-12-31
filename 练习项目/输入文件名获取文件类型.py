#输入文件名获取文件格式
import re
def gs(self):
    gs = ''
    if self != '' and bool(re.search(r".",self)):
        number = self.find(r'.')+1
        gs = self[number:]
        return gs
        print("文件名为：%s，文件格式为：%s" % (name,gs))
    else:
        return("输入完整文件名")

while True:
    name = input("输入完整文件名：")
    if gs(name) == "输入完整文件名":
        continue
    else:
        print("文件格式为：",gs(name))