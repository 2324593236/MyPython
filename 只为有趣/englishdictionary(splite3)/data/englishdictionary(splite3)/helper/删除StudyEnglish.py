###删除数据
import sqlite3#调用数据库模块
sqlite = sqlite3.connect("StudyEnglish.db")#连接数据库
cursor = sqlite.cursor()#创建游标连接
data = input("请输入要清除的数据(区分大小写)：")
sqlite1 = """
delete from dictionary where word=?;
"""
##sql语句删除记录
cursor.execute(sqlite1,(data,))#执行sql语句
cursor.close()#关闭游标连接
sqlite.commit()#提交事务
sqlite.close()#关闭有对象连接