# -*- coding: utf-8 -*- #
#Filename judgePrime.py  Python 质数判断

def judgeprime(a):
    num = a
    # 质数大于0
    if num > 1:
        for i in range(2,num):
            if num % i == 0:
                print('%d 不是质数' % num )
                print(i ,'乘以',num//i,'等于',num)
                break
        else:
            print('%d 是质数' % num)
    else:
        print('%d 不是质数' % num )

judgeprime(5)