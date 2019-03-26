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


