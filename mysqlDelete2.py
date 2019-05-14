# -*- coding: utf-8 -*-
# Filename mysqlDelete2.py
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="runa#2013",
    database="spring_db"
)
mycursor = mydb.cursor()

sql = "DELETE FROM sites WHERE name = %s"
na = ("ruoo", ) # 注意这个写的格式，因为元组一个元素就是这样注意,

mycursor.execute(sql,na)

mydb.commit()

print(mycursor.rowcount, " 条记录删除")