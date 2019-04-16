# -*- coding: utf-8 -*-
# @Time    : 2019/4/16 下午10:08
# @Author  : Meng Xiao
class Solution:
    def GetMissingNumber(self, numbers, length):
        if not numbers or length <= 0:
            return -1
        left = 0
        right = length - 1
        while left <= right:
            mid = (left + right) // 2
            if numbers[mid] != mid:
                if mid == 0 or numbers[mid-1] == mid - 1:
                    return mid
                right = mid - 1
            else:
                left = mid + 1
        if left == length:
            return length

