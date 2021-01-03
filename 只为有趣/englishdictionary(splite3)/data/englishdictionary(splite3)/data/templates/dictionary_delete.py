###删除功能模块
import sqlite3#调用数据库模块

def delete1(self):
    """"删除数据模块"""
    sqlite = sqlite3.connect("data/StudyEnglish.db")  # 连接数据库
    cursor = sqlite.cursor()  # 创建游标连接
    sql1 = """delete from dictionary where id=?;"""##sql语句删除记录
    cursor.execute(sql1,(self,))  # 执行sql语句
    cursor.close()  # 关闭游标连接
    sqlite.commit()  # 提交事务
    sqlite.close()  # 关闭有对象连接

