# -*- coding: utf-8 -*-
# Filename mysqlUpdate.py
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="runa#2013",
    database="spring_db"
)
mycursor = mydb.cursor()

sql = "UPDATE sites SET name = 'ZH' WHERE name = 'Taobao'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, " 条记录被修改")