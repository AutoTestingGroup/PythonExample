# -*- coding: utf-8 -*-
# Filename  sol.py
# 二次方程式 ax**2 + bx + c = 0
# a、b、c 用户提供，为实数，a ≠ 0

# 导入 cmath(复杂数学运算) 模块
import cmath
a = float(input('请输入a:'))
b = float(input('请输入b:'))
c = float(input('请输入c:'))

#计算
d = (b**2) - (4*a*c)
if a == 0:
    print('这不是二次方程，结束')
else:

    # 两种求解方式
    sol1 = (-b - cmath.sqrt(d)) / (2 * a)
    sol2 = (-b + cmath.sqrt(d)) / (2 * a)
    if d>0:
        print('根据判断条件△= %d ,方程有两个不相等的实数根 '%d )
    elif  d==0:
        print('根据判断条件△= %d ,方程有两个相等的实数根' %d )
    else:
        print('根据判断条件△= %d ,方程无实数根，但有2个共轭复根' %d )
    print('结果为 {0} 和 {1}'.format(sol1, sol2))


