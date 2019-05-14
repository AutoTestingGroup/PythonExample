# -*- coding: utf-8 -*-

import MySQLdb

# 打开数据库连接
db = MySQLdb.connect("localhost", "root", "runa#2013", "testdb", charset='utf8' )

# 使用cursor()方法获取操作游标
cursor = db.cursor()
# SQL 插入语句
FN = [['zhangsan','li',28,'M',2003],['qunhong','liu',27,'F',2103],['tianxuan','cao',20,'F',2023],['lei','li',28,'M',2203]]
for fnele in FN:
    fn = fnele[0]
    ln = fnele[1]
    ae = fnele[2]
    sx = fnele[3]
    ic = fnele[4]

    sql = "INSERT INTO employee(FIRST_NAME,\
        LAST_NAME, AGE, SEX, INCOME)\
        VALUES ('%s','%s','%s','%s','%s' )" % \
         (fn, ln, ae, sx, ic)
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