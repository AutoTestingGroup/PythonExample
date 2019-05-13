# -*- coding: utf-8 -*-
# Filename countELement.py   Python 计算元素在列表中出现的次数
print('**********  方法1for  **************')
def countelement(list,x):
    count = 0
    for ele in list:
        if(ele == x):
            count += 1
    return count

lst = [8, 6, 8, 10, 8, 20, 10, 8, 8]
x = 8
print(countelement(lst, x))

print('**********  方法2count函数  **************')
def countX(lst, x):
    return lst.count(x)


lst = [8, 6, 8, 10, 8, 20, 10, 8, 8]
x = 8
print(countX(lst, x))