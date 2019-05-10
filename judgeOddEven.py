# -*- coding: utf-8 -*-
#fileName judgeOddEven.py Python 判断奇数偶数
import random
def judgeOdd(num = 0):
    if num == 0:
        print('结束，0既不是奇数，也不是偶数')
    else:
        if num % 2 == 0:
            print(' %d 是偶数' % num)
        else:
            print(' %d 是奇数' % num)

judgeOdd(4)