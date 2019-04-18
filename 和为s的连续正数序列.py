# -*- coding: utf-8 -*-
# @Time    : 2019/4/18 下午7:41
# @Author  : Meng Xiao
class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        small, big = 1, 2
        res = []
        csum = small + big
        while small < big:
            if csum > tsum:
                csum -= small
                small += 1
            else:
                if csum == tsum:
                    res.append([i for i in range(small, big+1)])
                big += 1
                csum += big
        return res

