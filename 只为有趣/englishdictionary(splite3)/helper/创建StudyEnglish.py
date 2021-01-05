###创建计算机英语数据库
import sqlite3#调用pymysql数据库模块
sqlite = sqlite3.connect("../data/StudyEnglish.db")
cursor = sqlite.cursor()#生成游标对象
cursor.execute('drop table if exists dictionary')#如果数据表存在就删除数据表
sq1 = """
create table dictionary(
id INTEGER primary key autoincrement,
word varchar(225) not null,
comment varchar(225) not null,
study_sign blob default 0 not null,
study_time date default null
);
"""
"""
sqlite语句，如果不存在dictionary数据表就创建一个名为dictionary的数据表，
键id 整型最长10字节 设置为主键 不为空 自动递增，
键word 可变长字符串最长225字节 不为空，
键comment 可变长字符串最长225字节 不为空，
键sign 可变长字符串最长225字节 默认为空，
键time 日期类型 默认为空，
"""
cursor.execute(sq1)#执行sqlite语句
cursor.close()#关闭游标对象
sqlite.commit()#提交事务
sqlite.close()#关闭连接对象
