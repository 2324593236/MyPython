###增加数据
import sqlite3#调用pymysql数据库模块
import datetime#调用datetime时间模块
sqlite = sqlite3.connect("StudyEnglish.db")#连接数据库
cursor = sqlite.cursor()#生成游标对象
a_word = input("请输入要记录的单词：")
a_comment = input("请输入所记录单词的注释：")
data = (a_word,a_comment,str(datetime.datetime.now().date()))
sqlite1 = "insert into dictionary(word,comment,study_time) values(?,?,?)"

##增加数据库数据
#如果数据表存在就删除数据表
cursor.execute(sqlite1,data)#执行mysql语句
cursor.close()#关闭游标对象
sqlite.commit()#提交事务
sqlite.close()#关闭连接对象

