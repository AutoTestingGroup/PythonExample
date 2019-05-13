# -*- coding: utf-8 -*-
# Filename createCalendar.py  Python 生成日历
# 判断部分是我加的 可以去除，形成最最简单版本
import calendar

def createCal(yy,mm):
    yy = int(yy)
    mm = int(mm)
    if yy / 1000 >=0 and len(str(yy))== 4:
        if mm / 10 >=0 and len(str(mm))<= 2 and mm < 13:
            t = calendar.month(yy,mm)
            print(t)
        else:
            print('月份不符合要求')
    else:
        print('年份不符合要求')


# 显示日历
createCal(2019,6)