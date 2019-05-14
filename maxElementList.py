# -*- coding: utf-8 -*-
# Filename maxElementList.py  Python 查找列表中最大元素
print('***************  实例1  *******************')
list1 = [10, 20, 4, 45, 99]
list1.sort()
print(list1[-1])

print('***************  实例2  *******************')
list2 = [10, 20, 4, 45, 99]
min_ele = max(list2)
print(min_ele)


print('***************  实例3  *******************')
def maxelementlist(mylist):
    min_ele = max(mylist)
    return min_ele

list2 = [10, 20, 4, 45, 99]
print(maxelementlist(list2))