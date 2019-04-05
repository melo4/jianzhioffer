# -*- coding: utf-8 -*-
# @Time    : 2019/4/5 下午3:37
# @Author  : Meng Xiao
class Solution:
    def GetUglyNumber(self, index):
        if not index:
            return 0
        ugly_number = [1] * index
        next_index = 1
        index2 = 0
        index3 = 0
        index5 = 0
        while next_index < index:
            minValue = min(ugly_number[index2]*2, ugly_number[index3]*3, ugly_number[index5]*5)
            ugly_number[next_index] = minValue

            while ugly_number[index2] * 2 <= ugly_number[next_index]:
                index2 += 1
            while ugly_number[index3] * 3 <= ugly_number[next_index]:
                index3 += 1
            while ugly_number[index5] * 5 <= ugly_number[next_index]:
                index5 += 1
            next_index += 1
        return ugly_number
s = Solution()
print(s.GetUglyNumber(10))