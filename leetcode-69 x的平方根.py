# -*- coding: utf-8 -*-
# @Time    : 2019/6/20 19:52
# @Author  : Meng Xiao
class Solution:
    def mySqrt(self, x):
        if  x < 0:
            return
        left = 0
        right = x
        while right >= left:
            mid = (left + right) // 2
            if mid * mid > x:
                right = mid - 1
            elif mid * mid < x:
                left = mid + 1
            else:
                return mid
        return right