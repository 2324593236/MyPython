###查询功能模块
import sqlite3#调用数据库模块
def select1(self):#建立函数
    """"查询数据模块"""
    sqlite = sqlite3.connect("data/StudyEnglish.db")  # 建立游标连接
    cursor = sqlite.cursor()  # 创建游标连接
    sql1 = """select * from dictionary where id=? or word=? or comment=?;"""#SQL语句查询
    cursor.execute(sql1,(self,self,self))#执行SQL语句
    tuple1 = cursor.fetchall()
    cursor.close()  # 关闭游标连接
    sqlite.close()  # 关闭对象连接
    return tuple1