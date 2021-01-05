###修改功能模块
import sqlite3#调用数据库模块
import datetime#调用时间模块
def update1(self):#新建一个函数
    """修改数据模块"""
    sqlite = sqlite3.connect("data/StudyEnglish.db")  # 建立游标连接
    cursor = sqlite.cursor()  # 创建游标连接
    sql1 = """update dictionary set word=?,comment=?,study_sign=?,study_time=? where id=?;"""  # SQL语句查询
    cursor.execute(sql1,self)  # 执行SQL语句
    cursor.close()  # 关闭游标连接
    sqlite.commit()#提交事务
    sqlite.close()  # 关闭对象连接

