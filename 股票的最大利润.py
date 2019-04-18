# -*- coding: utf-8 -*-
# @Time    : 2019/4/18 下午9:45
# @Author  : Meng Xiao
class Solution:
    def maxDiff(self, numbers):
        if not numbers or len(numbers) < 2:
            return 0
        minD = numbers[0] # 保存前i-1个数字的最小值
        maxDiff = numbers[1] - minD
        for i in range(2, len(numbers)):
            if numbers[i-1] < minD:
                minD = numbers[i-1]
            curDiff = numbers[i] - minD
            if curDiff > maxDiff:
                maxDiff = curDiff
        return maxDiff
