# -*- coding: utf-8 -*-
# Filename mysqlSelect.py
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="runa#2013",
    database="spring_db"
)
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM sites")
myresult = mycursor.fetchall()  # fetchall() 获取所有记录
for x in myresult:
    print(x)