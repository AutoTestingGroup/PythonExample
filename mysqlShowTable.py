# -*- coding: utf-8 -*-
# Filename mysqlShowTable.py
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="runa#2013",
    database="heat_platform_db"
)
mycursor = mydb.cursor()
mycursor.execute("SHOW TABLES")
for x in mycursor:
    print(x)