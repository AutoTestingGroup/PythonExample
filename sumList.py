# -*- coding: utf-8 -*-
# Filename sumList.py   Python 计算列表元素之和

print('****************  实例1  ******************')
list1 = [11, 5, 17, 18, 23]
sum = 0
for ele in range(0,len(list1)):
     sum = sum + list1[ele]
print(sum)

print('****************  实例2 使用 while() 循环 ******************')
list2 = [11, 5, 17, 18, 23]
i = 0
sum = 0
while i < len(list2):
    sum = sum + list2[i]
    i += 1
print(sum)

print('****************  实例3 使用递归 ******************')
list1 = [11, 5, 17, 18, 23]
def sumOfList(list, size):
    if (size == 0):
        return 0
    else:
        return list[size - 1] + sumOfList(list, size - 1)
total = sumOfList(list1, len(list1))
print("列表元素之和为: ", total)


print('****************  实例4   ******************')
list1 = [11, 5, 17, 18, 23]
sum = 0
for ele in list1:
     sum = sum + ele
print(sum)