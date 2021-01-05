###查询数据
import sqlite3#调用数据库模块
sqlite = sqlite3.connect("StudyEnglish.db")#创建对象连接
cursor = sqlite.cursor()#创建游标连接
data = input("请输入要查询的单词：")
sqlite1 = """
select * from dictionary where id>0;
"""
##sql语句查询记录
cursor.execute(sqlite1)#执行SQL语句
print(cursor.fetchall())#输出查询记录
cursor.close()#关闭游标连接
sqlite.close()#关闭对象连接

