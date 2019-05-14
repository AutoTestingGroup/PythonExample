# -*- coding: utf-8 -*-
# Filename minElementList.py   Python 查找列表中最小元素
print('***************  实例1  *******************')
list1 = [10, 20, 4, 45, 99]
list1.sort()
print(list1[0])

print('***************  实例2  *******************')
list2 = [10, 20, 4, 45, 99]
min_ele =min(list2)
print(min_ele)


print('***************  实例3  *******************')
def minelementlist(mylist):
    min_ele = min(mylist)
    return min_ele

list2 = [10, 20, 4, 45, 99]
print(minelementlist(list2))