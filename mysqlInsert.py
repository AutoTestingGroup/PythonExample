# -*- coding: utf-8 -*-
# Filename mysqlInsert.py
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="runa#2013",
    database="spring_db"
)
mycursor = mydb.cursor()
sql = "INSERT INTO sites (name, url) VALUES (%s, %s)"
val = ("RUNOOB", "https://www.runoob.com")
mycursor.execute(sql, val)

mydb.commit()  # 数据表内容有更新，必须使用到该语句

print(mycursor.rowcount, "记录插入成功。")