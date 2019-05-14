# -*- coding: utf-8 -*-
# Filename dbUpdate.py
import MySQLdb

# 打开数据库连接
db = MySQLdb.connect("localhost", "root", "runa#2013", "testdb", charset='utf8' )
# 使用cursor()方法获取操作游标
cursor = db.cursor()
# SQL 更新语句
sql = "UPDATE EMPLOYEE SET AGE = AGE + 1 WHERE SEX = '%c'" % ('M')
try:
   # 执行SQL语句
   cursor.execute(sql)
   # 提交到数据库执行
   db.commit()
except:
   # 发生错误时回滚
   db.rollback()

# 关闭数据库连接
db.close()