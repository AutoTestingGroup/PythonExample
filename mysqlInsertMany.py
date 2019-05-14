# -*- coding: utf-8 -*-
# Filename mysqlInsertMany.py
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="runa#2013",
    database="spring_db"
)
mycursor = mydb.cursor()

sql = "INSERT INTO sites (name, url) VALUES (%s, %s)"
val = [
    ('Google', 'https://www.google.com'),
    ('Github', 'https://www.github.com'),
    ('Taobao', 'https://www.taobao.com'),
    ('stackoverflow', 'https://www.stackoverflow.com/'),
    ('ruoo',None )
# 重点是这个None，注意没有''
]
mycursor.executemany(sql, val)

mydb.commit()  # 数据表内容有更新，必须使用到该语句

print(mycursor.rowcount, "记录插入成功。")
