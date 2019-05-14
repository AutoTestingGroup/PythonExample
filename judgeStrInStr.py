# -*- coding: utf-8 -*-
# Filename judgeStrInStr.py  Python 判断字符串是否存在子字符串
print('***************   实例1  *****************')
str1 = 'springbocai'
str2 = 'bocai'
if str2 in str1:
    print(' %s 存在与 %s' % (str2,str1))
else:
    print('不存在')

print('***************   实例2  *****************')


def judgestrinstr(string, sub_str):
    if (string.find(sub_str) == -1):
        print("不存在！")
    else:
        print("存在！")

#调用函数
str1 = 'springbocai'
str2 = 'bocai'
judgestrinstr(str1,str2)



