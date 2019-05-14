# -*- coding: utf-8 -*-
# Filename judgeStrLen.py  Python 判断字符串长度
print('****************  实例1  ********************')
def judgestrlen(mystr):
    return len(mystr)

# 调用函数
str1 = 'springboai'
print(judgestrlen(str1))

print('****************  实例2 使用循环计算  ********************')


def findLen(str):
    counter = 0
    while str[counter:]:
        counter += 1
    return counter


str = "runoob"
print(findLen(str))