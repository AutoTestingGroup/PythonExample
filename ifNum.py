# -*- coding: utf-8 -*-
#Filename ifNum

import random

i = 0
L1 = []
L2 = []
L3 = []
#循环随机100次
while i < 100:
    t = random.randint(-100, 100)
#判断随机数字是正数、0、负数
    if t > 0:
        L1.append(t)

    elif t == 0:
        L2.append(t)

    else:
        L3.append(t)

    i += 1
print('产生了如下正数：',L1,'次数为：',len(L1))
print('产生了如下0：',L2,'次数为：',len(L2))
print('产生了如下负数：',L3,'次数为：',len(L3))