# -*- coding: utf-8 -*-
#Filename judgeYear.py Python 判断闰年
#year = int(input('请输入年份：'))

def judgeYear(year):
    a = year
    if (a % 4 == 0 and a % 100 != 0) or (a % 400 == 0):
        print('%d 是润年' % a )
    else:
        print('%d 不是润年' % a)

judgeYear(2342)
