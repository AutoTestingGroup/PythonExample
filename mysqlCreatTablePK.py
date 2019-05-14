# -*- coding: utf-8 -*-
# Filename mysqlCreatTablePK.py
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="runa#2013",
    database="spring_db"
)
mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE sites (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), url VARCHAR(255))")