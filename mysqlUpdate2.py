# -*- coding: utf-8 -*-
# Filename mysqlUpdate2.py
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="runa#2013",
    database="spring_db"
)
mycursor = mydb.cursor()


sql = "UPDATE sites SET name = %s WHERE name = %s"
val = ("ZH", "Github")
mycursor.execute(sql,val)

mydb.commit()

print(mycursor.rowcount, " 条记录被修改")