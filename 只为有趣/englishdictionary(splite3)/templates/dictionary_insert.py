###增添功能模块
import sqlite3
import datetime
def insert1(self):#建立函数
    """增添数据模块"""
    sqlite = sqlite3.connect("data/StudyEnglish.db")  # 建立游标连接
    cursor = sqlite.cursor()  # 创建游标连接
    sql1 = """insert into dictionary(word,comment,study_time) values(?,?,?);"""#SQL语句查询
    cursor.execute(sql1,self)#执行SQL语句
    cursor.close()  # 关闭游标连接
    sqlite.commit()  # 提交事务
    sqlite.close()  # 关闭对象连接
