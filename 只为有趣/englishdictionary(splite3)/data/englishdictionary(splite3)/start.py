###功能入口###
import sys,datetime
sys.path.append(r"templates")
from templates.dictionary_select import select1
from templates.dictionary_fetchall import fetchall1
from templates.dictionary_insert import insert1
from templates.dictionary_delete import delete1
from templates.dictionary_update import update1
if __name__ == "__main__":#定义一个主程序
    """本程序仅供个人使用"""
    while True:#死循环
        print(">>" * 10, "English_Dictionary", "<<" * 10, "\n")
        print("可执行操作如下：\n""\t1)查询 \t2)预览 \t3)增添 \t4)删除 \t5)修改 \t0)退出\n")
        a_start = input("请输入要执行的操作：\n")
        if a_start == '1':#查询功能判定
            while True:
                select_self = input("请输入要查找数据的ID或单词或注释\n(输入0结束操作):\n")  # 接收输入的值
                if select_self == '':  # 值为空时进入下一次循环
                    print("请正确输入")
                    continue
                elif select_self == '0':  # 值为0时跳出循环
                    break
                else:  # 否则
                    select_tuple = select1(select_self)
                if select_tuple == ():  # 如果函数返回的元组为空时提示并进入下一次循环
                    print("数据未存储(输入0结束操作)\n")
                    continue
                else:  # 否则
                    for item in select_tuple:  # 遍历查询结果返回的元组
                        print("所查单词：【ID：%s " % item[0], "单词：%s " % item[1], "注释：%s " % item[2], "标记%s " % item[3],
                              "时间%s】\n" % item[4])  # 输出遍历的元组
                    continue  # 进入下一次循环
            continue

        elif a_start == '2':#预览功能判定
            fetchall_self = ''  # 初始化变量
            while fetchall_self != '0':  # 当变量不为0时
                fetchall_self = input("1)按序列号顺序预览\n2)按字母大小写顺序预览\n0)退出\n")
                if fetchall_self == '1' or fetchall_self == '2':  # 当变量为1时
                    fetchall_list = fetchall1(fetchall_self)  # 执行fetchall函数
                    if fetchall_list == []:
                        print("数据库为空，请存储数据后再操作")
                        break
                    else:
                        for item in fetchall_list:   
                            print("ID：%s\t" % item[0], "单词：%s\t" % item[1], "注释：%s\t" % item[2],"标记%s\n" % item[3])  # 输出遍历的元组
                elif fetchall_self == '0':
                    break
                if fetchall_list == []:
                    break
                else:
                    print("请正确输入")
                    continue
            continue

        elif a_start == '3':#增添功能判定
            insert_word = ''  # 初始化变量
            while insert_word != '0':  # 当word不为0时
                insert_word = input("请输入要添加的单词(按0退出)：")  # 获取word值
                if insert_word == '0':
                    break
                insert_comment = input("请输入要添加的注释(按0退出)：")  # 获取comment值
                if insert_comment == '0':
                    break
                if insert_word != '' and insert_comment != '':  # 当获取的数据不为空时
                    study_time = datetime.datetime.now().date()  # 调用时间函数
                    insert_tuple1 = (insert_word, insert_comment, study_time)  # 建立SQL执行语句所需要的元组
                    insert1(insert_tuple1)  # 执行函数
                    insert_tuple2 = select1(insert_word,)  # 执行SQL语句
                    for item in insert_tuple2:  # 遍历查询结果返回的元组
                        print("新增单词：【ID：%s " % item[0], "单词：%s " % item[1], "注释：%s " % item[2], "标记%s " % item[3],"时间%s】\n" % item[4])  # 输出遍历的元组
                else:
                    print("请正确输入")
                    continue  # 进入下一循环
            continue

        elif a_start == '4':#删除功能判定
            delete_self = ''
            while delete_self != '0':
                delete_self = input("请输入要查找数据的ID或单词或注释\n(输入0结束操作):\n")  # 接收输入的值
                if delete_self == '':  # 值为空时进入下一次循环
                    print("请正确输入")
                    continue
                elif delete_self == '0':  # 值为0时跳出循环
                    break
                else:  # 否则
                    delete_tuple1 = select1(delete_self)
                if delete_tuple1 == ():  # 如果函数返回的元组为空时提示并进入下一次循环
                    print("数据未存储(输入0结束操作)\n")
                    continue
                else:  # 否则
                    for item in delete_tuple1:  # 遍历查询结果返回的元组
                        print("确认要删除的数据：【ID：%s " % item[0], "单词：%s " % item[1], "注释：%s " % item[2], "标记%s " % item[3],
                              "时间%s】" % item[4])  # 输出遍历的元组
                        delete_id = item[0]
                    delete_num = ''  # 初始化变量
                    while delete_num != '0':  # 当变量不为0时
                        delete_num = input("确认请回车(输入0结束操作)\n")
                        if delete_num == '':  # 当变量为空时
                            delete1(delete_id,)  # 执行delete函数
                            print("数据已删除或不存在")
                            break
                        elif delete_num == '0':
                            break
                        else:
                            print("请正确输入")
                            continue
                    if delete_num == '0':
                        break
                    else:
                        continue
            continue

        elif a_start == '5':#修改功能判定
            update_self = ''  # 初始化变量
            while update_self != '0':  # 当变量不为0时
                update_self = input("请输入要查找数据的ID或单词或注释\n(输入0结束操作):\n")  # 接收输入的值
                if update_self == '':  # 值为空时进入下一次循环
                    print("请正确输入(输入0结束操作)")
                    continue  # 进入下次循环
                elif update_self == '0':  # 值为0时跳出循环
                    break  # 跳出循环
                else:  # 否则
                    update_tuple = select1(update_self)  # 执行select函数并赋值给一个变量
                if update_tuple == ():  # 如果函数返回的元组为空时提示并进入下一次循环
                    print("数据未存储(输入0结束操作)\n")
                    continue
                else:  # 否则
                    for item in update_tuple:  # 遍历查询结果返回的元组
                        print("所查单词：【ID：%s " % item[0], "单词：%s " % item[1], "注释：%s " % item[2], "标记%s " % item[3],
                              "时间%s】\n" % item[4])  # 输出遍历的元组
                        oldid = item[0]  # 将元组中的数据赋值
                        oldword = item[1]
                        oldcomment = item[2]
                        oldsign = item[3]
                    print("\n请输入要修改的数据属性(输入0结束操作)")
                    newword = input("单词修改为(输入空跳过，输入0结束操作)：")
                    if newword == '0':  # 当输入变量为0时
                        break  # 跳出循环
                    elif newword:  # 当输入变量不为空时
                        oldword = newword  # 将输入变量赋值给要修改的参数
                    newcomment = input("注释修改为(输入空跳过，输入0结束操作)：")
                    if newcomment == '0':
                        break
                    elif newcomment:
                        oldcomment = newcomment
                    newsign = input("标记修改为(输入0或1，跳过输入回车)：")
                    if newsign == '0' or newsign == '1':
                        oldsign = newsign
                    else:
                        print("标记参数只能是0或1")
                        oldsign = oldsign
                    time1 = str(datetime.datetime.now().date())  # 获取当前时间参数
                    a = ''  # 初始化变量
                    while a != '0':  # 当变量不为0时
                        print("确认将数据修改为：【ID：%s " % oldid, "单词：%s " % oldword, "注释：%s " % oldcomment, "标记%s " % oldsign,
                              "时间%s】" % time1)  # 输出遍历的元组
                        a = input("确认请回车(输入0结束操作)\n")
                        if a == '':  # 当变量为空时
                            update1((oldword, oldcomment, oldsign, time1, oldid))  # 执行update函数
                            print("数据修改完成")
                            break
                        else:
                            print("请正确输入")
                            continue
                    if a == '0':
                        break
                    else:
                        continue
            continue

        elif a_start == '0':#退出功能判定
            print(">>" * 7, "欢迎下次使用EnglishDictionary", "<<" * 7, "\n")
            break
        else:
            print("\n>>>>>>>>>>请正确输入<<<<<<<<<<\n")
            continue
