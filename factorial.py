# -*- coding: utf-8 -*-
#Filename factorial.py  Python 阶乘实例

num = int(input('请输入需要阶乘的数：'))
factorial = 1
if num < 0:
    print('负数没有阶乘')
elif num == 0:
    print('0的阶乘为1')
else:
    for i in range(1,num+1):
        factorial = factorial * i
    print('%d 的阶乘为 %d'%(num,factorial))


