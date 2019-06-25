# -*- coding: utf-8 -*-
# @Time    : 2019/6/25 19:58
# @Author  : Meng Xiao
class Solution:
    def removeDuplicates(self, nums):
        if len(nums) <= 1:
            return len(nums)
        slow = 0
        for i in range(1, len(nums)):
            if nums[slow] != nums[i]:
                slow += 1
                nums[slow] = nums[i]

        return slow + 1