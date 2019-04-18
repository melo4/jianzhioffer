# -*- coding: utf-8 -*-
# @Time    : 2019/4/14 下午7:36
# @Author  : Meng Xiao

class Solution:
    '''
    方法1 非动态规划
    '''
    def maxSum(self, alist):
        if not alist:
            return
        max_value = alist[0]
        tmpSum = alist[0]
        for i in range(1, len(alist)):
            if tmpSum < 0:
                tmpSum = alist[i]
            else:
                tmpSum += alist[i]
            if tmpSum > max_value:
                max_value = tmpSum
        return max_value
    '''
    方法2 动态规划 dp[i]表示以第i结尾的的子数组中子数组的最大和
    '''
    def maxSumdp(self, alist):
        if not alist:
            return
        max_value = alist[0]
        dp = [0] * (len(alist)+1)
        dp[0] = alist[0]
        for i in range(1, len(alist)):
            if dp[i-1] < 0:
                dp[i] = alist[i]
            else:
                dp[i] = dp[i-1] + alist[i]
            if dp[i] > max_value:
                max_value = dp[i]
        return max_value



s = Solution()
print(s.maxSumdp([-2,-8,-1,-5,-9]))
