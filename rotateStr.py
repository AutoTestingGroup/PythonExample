# -*- coding: utf-8 -*-
# Filename rotateStr.py   Python 对字符串切片及翻转
def rotate(input, d):
    Lfirst = input[0: d]
    Lsecond = input[d:]
    Rfirst = input[0: len(input) - d]
    Rsecond = input[len(input) - d:]

    print("头部切片翻转 : ", (Lsecond + Lfirst))
    print("尾部切片翻转 : ", (Rsecond + Rfirst))


if __name__ == "__main__":
    input = 'springbocai'
    d = 2  # 截取两个字符
    rotate(input, d)