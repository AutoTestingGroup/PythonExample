# -*- coding: utf-8 -*-
# Filename moveStr.py  Python 移除字符串中的指定位置字符
print('****************    实例1     *************************')
old_str = 'springbocai'
print("原始字符串为 : " + old_str)

# 定义新的字符串
new_str = ''
for i in range(0,len(old_str)):
    if i != 2:
        new_str = new_str + old_str[i]
print("新字符串为 : " + new_str)


print('****************    实例2   *************************')


def movestr(mystr,x):
    new_str = ''
    for i in range(0,len(mystr)):
        if x > len(mystr):
            print('指定移除元素超出长度！')
            break
        elif i != x:
            new_str = new_str + mystr[i]
    return new_str

old_str = 'springbocai'
print( movestr(old_str,2))