# -*- coding: utf-8 -*-
# Filename mysqlCreatTablePK.py
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="runa#2013",
    database="testdb"
)
mycursor = mydb.cursor()

mycursor.execute("ALTER TABLE employee ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")