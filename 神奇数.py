# -*- coding: utf-8 -*-
# @Time    : 2019/8/31 15:27
# @Author  : Meng Xiao
'''
给出一个区间[a, b]，计算区间内“神奇数”的个数。
神奇数的定义：存在不同位置的两个数位，组成一个两位数（且不含前导0），且这个两位数为质数。
比如：153，可以使用数字3和数字1组成13，13是质数，满足神奇数。同样153可以找到31和53也为质数，只要找到一个质数即满足神奇数。
'''
import itertools
a, b = map(int, input().split())
zs = [11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
# 所有两位的质数
num = 0
for i in range(a, b+1):
    tt = list(str(i))
    for item in itertools.combinations(tt, 2):
        tep = [int(''.join(item)), int(''.join(item[::-1]))]
        for j in tep:
            if j in zs and j >= 10:
                num += 1
                break
            else:
                continue
print(num)
