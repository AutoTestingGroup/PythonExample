# -*- coding: utf-8 -*-

# CGI处理模块
import MySQLdb
db = MySQLdb.connect(host='localhost',port=3306,user='root',passwd='runa#2013',db='testdb',charset='utf8')
#使用cursor()方法获取操作游标
cursor = db.cursor()
# 使用execute方法执行SQL语句
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
# # 创建数据表SQL语句
sql = """CREATE TABLE EMPLOYEE (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,
         SEX CHAR(1),
         INCOME FLOAT )"""
#执行SQL语句
cursor.execute(sql)
print('创建数据库成功')
# SQL 插入语句
sql1 = """INSERT INTO EMPLOYEE(FIRST_NAME,
         LAST_NAME, AGE, SEX, INCOME)
         VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""



try:
   # 执行sql语句
   cursor.execute(sql1)

   # 提交到数据库执行
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()


# 关闭数据库连接
db.close()