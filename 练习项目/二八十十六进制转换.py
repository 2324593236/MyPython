if __name__ == "__main__" :
    while True:
        try:
            print("请输入要转换的进制类型\n")
            number_start = input("\na)二进制\tb)八进制\tc)十进制\td)十六进制\t#)退出\n")
            if number_start == '#':
                break
            elif number_start == "a":
                number1 = input("输入要转化的二进制数字：")
                number_start2 = input("\n输入要转化为的进制类型\tb)八进制\tc)十进制\td)十六进制\t#)退出\n")
                if number_start2 == "#":
                    break
                elif number_start2 == "b":
                    number2 = oct(ecal(number1))
                    print("输入的二进制数字为：", number1, "转化为八进制数字为：", number2)
                elif number_start2 == "c":
                    number2 = int(eval(number1))

                    print("输入的二进制数字为：", number1, "转化为十进制数字为：", number2)
                elif number_start2 == "d":
                    number2 = hex(eval(number1))
                    print("输入的二进制数字为：", number1, "转化为十六进制数字为：", number2)
                else:
                    print("请正确输入")
                    continue
                continue
            elif number_start == "b":
                number1 = input("输入要转化的八进制数字：")
                number_start2 = input("\n输入要转化为的进制类型\ta)二进制\tc)十进制\td)十六进制\t#)退出\n")
                if number_start2 == "#":
                    break
                elif number_start2 == "a":
                    number2 = bin(eval(number1))
                    print("输入的八进制数字为：", number1, "转化为二进制数字为：", number2)
                elif number_start2 == "c":
                    number2 = int(eval(number1))
                    print("输入的八进制数字为：", number1, "转化为十进制数字为：", number2)
                elif number_start2 == "d":
                    number2 = hex(eval(number1))
                    print("输入的八进制数字为：", number1, "转化为十六进制数字为：", number2)
                else:
                    print("请正确输入")
                    continue
                continue
            elif number_start == "c":
                number1 = input("输入要转化的十进制数字：")
                number_start2 = input("\n输入要转化为的进制类型\ta)二进制\tb)八进制\td)十六进制\t#)退出\n")
                if number_start2 == "#":
                    break
                elif number_start2 == "a":
                    number2 = bin(eval(number1))
                    print("输入的十进制数字为：", number1, "转化为二进制数字为：", number2)
                elif number_start2 == "b":
                    number2 = oct(eval(number1))
                    print("输入的十进制数字为：", number1, "转化为十进制数字为：", number2)
                elif number_start2 == "d":
                    number2 = hex(eval(number1))
                    print("输入的十进制数字为：", number1, "转化为十六进制数字为：", number2)
                else:
                    print("请正确输入")
                    continue
                continue
            elif number_start == "d":
                number1 = input("输入要转化的十六进制数字：")
                number_start2 = input("\n输入要转化为的进制类型\ta)二进制\tb)八进制\tc)十进制\t#)退出\n")
                if number_start2 == "#":
                    break
                elif number_start2 == "a":
                    number2 = bin(eval(number1))
                    print("输入的十六进制数字为：", number1, "转化为二进制数字为：", number2)
                elif number_start2 == "b":
                    number2 = oct(eval(number1))
                    print("输入的十六进制数字为：", number1, "转化为八进制数字为：", number2)
                elif number_start2 == "c":
                    number2 = int(eval(number1))
                    print("输入的十六进制数字为：", number1, "转化为十进制数字为：", number2)
                    continue
                else:
                    print("请正确输入")
                    continue
            else:
                print("请正确输入")
        except (ValueError,NameError):
            print("请正确输入")
            continue
