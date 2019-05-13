# -*- coding: utf-8 -*-
# Filename  overturnList.py  Python 数组翻转指定个数的元素
'''

定义一个整型数组，并将指定个数的元素翻转到数组的尾部。
例如：(ar[], d, n) 将长度为 n 的 数组 arr 的前面 d 个元素翻转到数组尾部。
以下演示了将数组的前面两个元素放到数组后面。
原始数组:
1 2 3 4 5 6 7
翻转后：
3 4 5 6 7 1 2
'''


def leftRotate(arr, d, n):
    for i in range(d):
        leftRotatebyOne(arr, n)


def leftRotatebyOne(arr, n):
    temp = arr[0]
    for i in range(n - 1):
        arr[i] = arr[i + 1]
    arr[n - 1] = temp


def printArray(arr, size):
    for i in range(size):
        print("%d" % arr[i], end=" ")


arr = [1, 2, 3, 4, 5, 6, 7]
leftRotate(arr, 2, 7)
printArray(arr, 7)

