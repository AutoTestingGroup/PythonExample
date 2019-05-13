# -*- coding: utf-8 -*-
# Filename file.py  Python 文件 IO 包括 open，read，write
# 写文件

with open("test.txt", "wt") as out_file:
    out_file.write("该文本会写入到文件中\n看到我了吧！")


# Read a file
with open("test.txt", "rt") as in_file:
    text = in_file.read()

print(text)