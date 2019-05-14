# -*- coding: utf-8 -*-

import MySQLdb

# 打开数据库连接
db = MySQLdb.connect("localhost", "root", "runa#2013", "testdb", charset='utf8' )

# 使用cursor()方法获取操作游标
cursor = db.cursor()
# SQL 插入语句
FN = ['qunqun','lihua','sansan','yuyu','xiaom']
for fnele in FN:
      sql = "INSERT INTO employee(FIRST_NAME,\
            LAST_NAME, AGE, SEX, INCOME)\
            VALUES ('%s','%s','%s','%s','%s' )" % \
             (fnele, 'machel', 20, 'M', 2000)
      # 不加''会不执行commit 进行 会进行回滚rollback操作
      try:
         # 执行sql语句
         cursor.execute(sql)
         # 提交到数据库执行
         db.commit()
      except:
         # 发生错误时回滚
         db.rollback()

# 关闭数据库连接
db.close()