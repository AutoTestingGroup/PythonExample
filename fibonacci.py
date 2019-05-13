# -*- coding: utf-8 -*-
#Filename fibonacci  Python 斐波那契数列

# 获取用户输入
num = int(input('要获取第几项的值：'))

# 第一和第二项
n1 = 0
n2 = 1
i = 2
#判断输入是否合法
if num <= 0:
    print('请输入合法的正整数！')
elif num ==1:
    print("斐波那契数列：")
    print(n1)
else:
    print("斐波那契数列：")
    print(n1,' , ',n2,end = ' , ')
    while  i < num:
        nth = n1 + n2
        print(nth ,end = ' , ')
        #更新值
        n1= n2
        n2 = nth
        i += 1