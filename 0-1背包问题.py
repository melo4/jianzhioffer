# -*- coding: utf-8 -*-
# @Time    : 2019/6/11 19:41
# @Author  : Meng Xiao
'''
输入：
第一行是一个正整数，表示总容量
第二行是一个长度为n的数组，代表物品重量
第三行是一个长度为n的数组，代表物品价值
输出：
最大价值
example:
1000
200 600 100 180 300 450
6 10 3 4 5 8
output: 21
'''
import numpy as np
# 0-1背包
class Solution:
    def bag0_1(self, wlist, vlist, totalWeight):
        totalLength = len(vlist) # 表示物品的数量
        dpArr = np.zeros((totalLength+1, totalWeight+1), dtype=np.int32)
        for i in range(1, totalLength+1):
            for j in range(1, totalWeight+1):
                if wlist[i-1] <= j:
                    dpArr[i][j] = max(dpArr[i-1][j], dpArr[i-1][j-wlist[i-1]]+vlist[i-1])
                else:
                    dpArr[i][j] = dpArr[i-1][j]
        return dpArr[-1][-1]

