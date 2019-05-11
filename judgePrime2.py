# -*- coding: utf-8 -*-
#Filename judgePrime2.py Python 输出指定范围内的素数

def judgePrime2(lower,upper):

    for num in range(lower, upper + 1):
        # 素数大于 1
        # if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                print(num)
judgePrime2(1,100,)