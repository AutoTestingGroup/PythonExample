# -*- coding: utf-8 -*-
# Filename sumDict.py  Python 计算字典值之和
def returnSum(myDict):
    sum = 0
    for i in myDict:
        sum = sum + myDict[i]

    return sum


dict = {'a': 100, 'b': 200, 'c': 300}
print("Sum :", returnSum(dict))