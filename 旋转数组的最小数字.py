# -*- coding: utf-8 -*-
# @Time    : 2019/3/26 下午8:20
# @Author  : Meng Xiao
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        if len(rotateArray) == 0:
            return 0
        front = 0
        rear = len(rotateArray) - 1
        minVal = rotateArray[0]

        if rotateArray[front] < rotateArray[rear]:
            return rotateArray[front]
        else:
            while rear - front > 1:
                mid = (front + rear) // 2
                if rotateArray[mid] >= rotateArray[front]:
                    front = mid
                elif rotateArray[mid] <= rotateArray[rear]:
                    rear = mid
                elif rotateArray[front] == rotateArray[mid] == rotateArray[rear]:
                    for i in range(1, len(rotateArray)):
                        if rotateArray[i] < minVal:
                            minVal = rotateArray[i]


            minVal = rotateArray[rear]
        return minVal



# leetcode-33搜索旋转排序数组
class Solution2:
    def search(self, nums, target):
        if not nums:
            return -1
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[left]:
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1

