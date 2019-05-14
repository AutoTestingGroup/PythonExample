# -*- coding: utf-8 -*-
# Filename mysqlConnect.py
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",  # 数据库主机地址
    user="root",  # 数据库用户名
    passwd="runa#2013",   # 数据库密码
    database="spring_db" # 数据库
)

print(mydb)