# -*- coding: utf-8 -*-
# Filename mysqlDropTable.py
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="runa#2013",
    database="spring_db"
)
mycursor = mydb.cursor()

sql = "DROP TABLE IF EXISTS sites"  # 删除数据表 sites

mycursor.execute(sql)