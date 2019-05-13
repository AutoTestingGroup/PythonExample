# -*- coding: utf-8 -*-
#filename DecimalToBOH.py   Python 十进制转二进制、八进制、十六进制

num = int(input('请输入一个十进制的数：'))

print("十进制数为：", num)
print("转换为二进制为：", bin(num))
print("转换为八进制为：", oct(num))
print("转换为十六进制为：", hex(num))