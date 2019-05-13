# -*- coding: utf-8 -*-
# Filename sumOfCubes.py  Python 计算 n 个自然数的立方和
'''
实现要求：
输入 : n = 5
输出 : 225
公式 : 13 + 23 + 33 + 43 + 53 = 225

输入 : n = 7
输入 : 784
公式 : 13 + 23 + 33 + 43 + 53 + 63 + 73 = 784
'''

print( '************ 这是我使用递归写的 *********' )
def sumOfSeries(n):
    if n == 1:
        sum = 1
        return sum
    else:
        sum = n*n*n + sumOfSeries(n-1)
        return sum

# 调用函数
print(sumOfSeries(5))

print( '************ for 循环 *********' )
# 定义立方和的函数
def sumOfCubes(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i * i * i

    return sum
# 调用函数
print(sumOfCubes(5))
