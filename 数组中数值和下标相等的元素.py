# -*- coding: utf-8 -*-
# @Time    : 2019/4/16 下午10:20
# @Author  : Meng Xiao
class Solution:
    def GetNUmberSameAsIndex(self, numbers):
        length = len(numbers)
        if not numbers or length <= 0:
            return
        left = 0
        right = length - 1
        while left <= right:
            mid = (left + right) // 2
            if numbers[mid] == mid:
                return mid
            if numbers[mid] > mid:
                right = mid - 1
            else:
                left = mid + 1

        return
s = Solution()
print(s.GetNUmberSameAsIndex([-3,-1,1,3,5]))