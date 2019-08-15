# -*- coding: utf-8 -*-
# @Time    : 2019/6/3 20:00
# @Author  : Meng Xiao
class Solution:
    def maxArea(self, height):
        ans = left = 0
        right = len(height) - 1
        while left < right:
            ans = max(ans, (right-left) * min(height[left], height[right]))
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
            return ans