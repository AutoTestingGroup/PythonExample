# -*- coding: utf-8 -*-
# Filename locationList.py  Python 将列表中的指定位置的两个元素对调

def swapPositions(list, pos1, pos2):
    list[pos1],list[pos2] = list[pos2],list[pos1]
    return list


List = [23, 65, 19, 90]
pos1, pos2 = 1, 3

print(swapPositions(List, pos1 - 1, pos2 - 1))