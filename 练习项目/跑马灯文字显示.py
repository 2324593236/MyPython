import os
import time
values = input("输入要显示的内容：")
values = "+"*10+values+"+"*10
if values:
    while True:
        os.system('cls')
        print(values)
        time.sleep(0.1)
        values = values[1:] + values[0]