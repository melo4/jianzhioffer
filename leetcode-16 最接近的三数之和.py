# -*- coding: utf-8 -*-
# @Time    : 2019/6/17 19:48
# @Author  : Meng Xiao
class Solution:
    def threeSumClosest(self, nums, target):
        if not nums or not target or len(nums) < 3:
            return
        nums.sort()
        res = nums[0] + nums[1] + nums[2]
        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                tsum = nums[i] + nums[j] + nums[k]
                if abs(tsum - target) < abs(res - target):
                    res = tsum
                if tsum < target:
                    j += 1
                elif tsum > target:
                    k -= 1
                else:
                    j += 1
                    k -= 1

        return res