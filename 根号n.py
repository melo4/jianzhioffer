# -*- coding: utf-8 -*-
# @Time    : 2019/8/22 21:05
# @Author  : Meng Xiao
'''
求解根号n,
'''

# 二分法
def mySqrt1(x):
    if x <= 0:
        return 0
    min_F = 0.001
    begin = float(1)
    end = x / 2 + 1
    mid = begin + (end-begin) / 2
    while (end-begin) > min_F:
        if (x-mid*mid) > min_F:
            begin = mid
        elif (mid*mid-x) > min_F:
            end = mid
        elif abs(x-mid*mid) < min_F:
            break
        mid = begin + (end-begin) / 2
    print(x-mid*mid)
    return mid




# 梯度下降法
def mySqrt2(x):
    if x <= 0:
        return 0
    lr = 0.001 # 学习率
    cur = 1
    for i in range(10000):
        tmp = 4 * cur * (cur*cur-x)
        cur -= lr * tmp
    return cur


# 牛顿法
'''
 x^2 = a的解，也就是函数f(x) = x^2 – a与x轴的交点。
 可以在x轴上先任选一点x0，则点（x0, f(x0)）在f(x)上的切线，
 与x轴的交点为x1，它们满足切线的方程：f(x0)=(x0-x1)f’(x0)，
 可得x1更接近最终的结果，解方程得到：x1 = (x0 + (a/x0))/2。
 以x1为新的x0，按照切线的方法依次迭代下去，最终求得符合精确度要求的结果值。
'''
def mySqrt3(x):
    if x <= 0:
        return 0
    res = x
    last_res = 0
    min_F = 0.001
    while abs(res-last_res) > min_F:
        last_res = res
        res = (res+x/res)/2
    return res
print(mySqrt3(8))