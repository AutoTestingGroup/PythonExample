# -*- coding: utf-8 -*-
# Filename flipList.py Python 翻转列表
print('***********  实例1  ************')
def Reverse(lst):
    lst.reverse()
    return lst
lst = [10, 11, 12, 13, 14, 15]
print(Reverse(lst))

print('\n','***********  实例2  ************')

def Reverse(lst):
    return [ele for ele in reversed(lst)]

lst = [10, 11, 12, 13, 14, 15]
print(Reverse(lst))

print('\n','***********  实例3  ************')
def Reverse(lst):
    new_lst = lst[::-1]
    return new_lst


lst = [10, 11, 12, 13, 14, 15]
print(Reverse(lst))