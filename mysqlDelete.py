# -*- coding: utf-8 -*-
# Filename mysqlDelete.py
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="runa#2013",
    database="spring_db"
)
mycursor = mydb.cursor()

sql = "DELETE FROM sites WHERE name = 'stackoverflow'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, " 条记录删除")