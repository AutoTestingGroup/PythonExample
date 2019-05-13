# -*- coding: utf-8 -*-
#Filename judgeELementList.py  Python 判断元素是否在列表中存在

print('*******  方法一  ******')
list = [ 1, 6, 3, 5, 3, 4 ]
print("查看 4 是否在列表中 ( 使用循环 ) : ")
for i in list:
    if(i == 4):
        print('存在')
print("查看 4 是否在列表中 ( 使用 in 关键字 ) : ")

if (4 in list):
    print ("存在")

print('*******  方法二  ******')
def judgeelementlist(list,element):
    print("查看 4 是否在列表中 ( 使用循环 ) : ")
    for i in list:
        if (i == element):
            print('存在')

list = [1, 6, 3, 5, 3, 4]
judgeelementlist(list,4)