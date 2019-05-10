# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
# Filename  sum.py  Python 数字求和
# 该实例输入2个数字，求和


print('***************方法一*******************')
# 用户输入数字
num1 = float(input('请输入第一个数:'))
num2 = float(input('请输入第二个数:'))

#求和
sum = num1 + num2
# 显示计算结果

print('第一个数字 %f , 第二个数字  %f 相加的和 %f '% (num1,num2,sum))


print('***************方法二*******************')
# 用户输入数字
num1 = input('请输入第一个数:')
num2 = input('请输入第二个数:')

#求和
sum = float(num1) + float(num2)
# 显示计算结果

print('数字 {0} 和 {1} 相加结果为： {2}'.format(num1, num2, sum))
print('第一个数字 {0} , 第二个数字  {1} 相加的和 {2} '.format(num1,num2,sum))

print('***************方法三*******************')
print('两数字之和为： %.1f '% (float(input('请输入第一个数:'))+float(input('请输入第一个数:'))))