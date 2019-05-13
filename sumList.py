# -*- coding: utf-8 -*-
# Filename sumList.py  Python 计算数组元素之和
print('***************** 使用sum *****************')
# 定义函数，arr 为数组，n 为数组长度，可作为备用参数，这里没有用到
def _sum(arr, n):

    # 使用内置的 sum 函数计算
    return (sum(arr))


# 调用函数
# 数组元素
arr = [12, 3, 4, 15]
# 计算数组元素的长度
n = len(arr)
ans = _sum(arr, n)
# 输出结果
print('数组元素之和为', ans)

print('***************** 使用for *****************')
arr = [12, 3, 4, 15]
sum = 0
for i in arr:
    sum += i
print(sum)
