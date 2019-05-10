# -*- coding: utf-8 -*-
# Filename square.py
# 已知三边求三角形面积，根据海伦公式

a = float(input('请输入a:'))
b = float(input('请输入b:'))
c = float(input('请输入c:'))

if a <= 0 or b <= 0 or c <=0:
    print('边长不能小于等于0')
elif a + b < c or a + c< b or b + c < a:
    print('两边之和小于第三边，这不是三角形')

else:

    # 求半周长
    s = (a +b +c)/2

    #求面积
    area = (s * (s - a) * (s - b) * (s - c))**0.5
    print('三角形面积为 %0.2f' %area)