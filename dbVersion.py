# -*- coding: utf-8 -*-

# CGI处理模块
import MySQLdb
db = MySQLdb.connect(host='localhost',port=3306,user='root',passwd='runa#2013',db='testdb',charset='utf8')
#使用cursor()方法获取操作游标
cursor = db.cursor()
# 使用execute方法执行SQL语句
cursor.execute("SELECT VERSION()")
# 使用 fetchone() 方法获取一条数据
data = cursor.fetchone()
print ("Database version : %s " % data)
# 关闭数据库连接
db.close()