# -*- coding: utf-8 -*-
# Filename getYesterday.py Python 获取昨天日期
import datetime
def getyesterday():
    today = datetime.date.today()

    oneday = datetime.timedelta(days=1)  # -1 就是明天
    yesterday = today - oneday
    return  yesterday

print(getyesterday())