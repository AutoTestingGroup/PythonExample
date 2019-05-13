# -*- coding: utf-8 -*-
# Filename  copyList.py  Python 复制列表

def clone_list(L1):
    L = L1[:]
    return  L

L1 = [4, 8, 2, 10, 15, 18]
L_copy = clone_list(L1)
print(L_copy)
