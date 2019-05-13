# -*- coding: utf-8 -*-
# Filename beginningEndTuple.py   Python 将列表中的头尾两个元素对调
print('*************  实例1  ***********')

def swapList(newList):
    size = len(newList)
    temp = newList[0]
    newList[0] = newList[size - 1]
    newList[size - 1] = temp
    return newList
#调用函数
newList = [1, 2, 3]
print(swapList(newList))

print('*************  实例2  ***********')


def swapList(newList):
    newList[0], newList[-1] = newList[-1], newList[0]

    return newList

#调用函数
newList = [1, 2, 3]
print(swapList(newList))


print('*************  实例3  ***********')


def swapList(newList):

    temp = newList[0]
    newList[0] = newList[-1]
    newList[-1] = temp
    return newList

#调用函数
newList = [1, 2, 3]
print(swapList(newList))

print('*************  实例4  ***********')


def swapList(list):
    get = list[-1], list[0]
    list[0], list[-1] = get
    return list
#调用函数
newList = [1, 2, 3]
print(swapList(newList))