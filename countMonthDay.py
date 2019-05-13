# -*- coding: utf-8 -*-
# Filename countMonthDay.py Python 计算每个月天数


import calendar

def countmonthday(yy,mm):
    count = calendar.monthrange(yy,mm)
    print(count)


countmonthday(2019,5)