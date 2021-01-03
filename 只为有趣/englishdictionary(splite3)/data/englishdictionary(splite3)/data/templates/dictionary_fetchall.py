###预览功能模块
import sqlite3
def fetchall1(self):
    """预览数据模块"""
    sqlite = sqlite3.connect("data/StudyEnglish.db")#建立游标连接
    cursor = sqlite.cursor()#创建游标连接
    sql1 = """select * from dictionary where id!=0;"""#SQL语句查询
    cursor.execute(sql1)#执行SQL语句
    tuple1 = cursor.fetchall()#数据库数据元组
    list1 = []#定义一个空列表
    self = int(self)#将传递的参数转换为整型
    self = self - 1
    for item in tuple1:#遍历数据库数据元组
        list1.append(item[self])#将遍历的项添加入列表里
        list1 = sorted(list1)#将列表里的信息按照从大到小，从a-z的顺序排列
    sql2 = """select * from dictionary where id=? or word=?;"""#SQL语句查询
    list2 = []#定义一个空列表
    for i in list1:#遍历传递的列表参数
        cursor.execute(sql2,(i,i))#执行SQL语句，
        tuple1 = cursor.fetchone()#遍历查询结果返回的元组
        list2.append(tuple1)#将遍历的元组添加如列表中
    cursor.close()#关闭游标连接
    sqlite.close()#关闭对象连接
    return list2#返回处理过的列表