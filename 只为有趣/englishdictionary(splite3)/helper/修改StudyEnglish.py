###修改数据
import sqlite3#调用数据库模块
import sys
sqlite = sqlite3.connect("StudyEnglish.db")#建立对象连接
cursor = sqlite.cursor()#创建游标连接
while True:
    data1 = input("请输入要修改的单词：")
    if data1 == '':
        print("请正确输入")
        continue
    else:
        sqlite1 = """
        select * from dictionary where (id=? or word=? or comment=?);
        """
        ##sql语句查询word或comment为指定值的id
        cursor.execute(sqlite1,(data1,data1,data1))
        break
for item in cursor.fetchall():
    print("ID：%s\t" % item[0],"单词：%s\t" % item[1],"注释：%s\t" % item[2])
    id = item[0]
word = input("单词改为(不修改的话略过)：")
comment = input("注释改为(不修改的话略过)：")
if word != '' and comment != '':        
    data2 = (word,comment,int(id))
    sqlite2 = """
    update dictionary set word=?,comment=? where id=?;
    """
    cursor.execute(sqlite2,data2)
elif word != '' and comment == '':
    data2 = (word,(id,))
    sqlite2 = """
    update dictionary set word=? where id=?;
    """
    cursor.execute(sqlite2,data2)
elif comment != '' and word == '':
    data2 = (comment,(id,))
    sqlite2 = """
    update dictionary set comment=? where id=?;
    """
    cursor.execute(sqlite2,data2)
elif comment == '' and word == '':
    pass
sqlite.commit()
sqlite3 = """
select * from dictionary where id=?;
"""
cursor.execute(sqlite3,(id,))
for item in cursor.fetchall():
    print("修改后\n""ID：%s\t" % item[0],"单词：%s\t" % item[1],"注释：%s\t" % item[2])
cursor.close()
sqlite.commit()
sqlite.close()
