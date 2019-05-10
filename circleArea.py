# -*- coding: utf-8 -*-
# Filename circleArea.py Python 计算圆的面积
# 计算圆面积


import math

print('*****方法一***********')
r = float(input('请输入圆半径r:'))

if r <=0:
    print('这不是圆形')
else:
    area = math.pi*r*r

    print('圆的面积为 %0.2f' % area)

print('*****  方法二,这里我调用了方法一输入的r  ***********')

def findarea(r):
    area = math.pi*r*r
    return area

print(findarea(r))
