# -*- coding: utf-8 -*-
# Filename dbDelete.py
import MySQLdb


# 打开数据库连接
db = MySQLdb.connect("localhost", "root", "runa#2013", "testdb", charset='utf8' )
# 使用cursor()方法获取操作游标
cursor = db.cursor()
# SQL 删除语句
sql = "DELETE FROM EMPLOYEE WHERE AGE > %s" % (20)
try:
   # 执行SQL语句
   cursor.execute(sql)
   # 提交修改
   db.commit()
except:
   # 发生错误时回滚
   db.rollback()

# 关闭连接
db.close()