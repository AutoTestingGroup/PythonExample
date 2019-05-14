# -*- coding: utf-8 -*-
# Filename mysqlCreatDatabase.py
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="runa#2013"
)
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE spring_db")