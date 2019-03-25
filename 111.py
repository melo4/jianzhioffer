# -*- coding: utf-8 -*-
# @Time    : 2019/3/25 下午1:47
# @Author  : Meng Xiao
def squareD(n):
    low = 0
    if n < 1:
        high = 1
    else:
        high = n
    mid = (low + high) / 2
    last = 0
    while(abs(mid - last) > 1e-10):
        if (mid*mid) > n:
            high = mid
        else:
            low = mid
        last = mid
        mid = (high+low) / 2

    return mid
print(squareD(25))