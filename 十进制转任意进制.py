# -*- coding: utf-8 -*-
# @Time    : 2019/9/21 20:30
# @Author  : Meng Xiao
def func2(n, x):
    a = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    b = []
    while True:
        s = n // x
        y = n % x
        b = b + [y]
        if s == 0:
            break
        n = s
    b.reverse()
    res = []
    for i in b:
        res.append(a[i])
    return ''.join(res)