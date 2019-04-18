# -*- coding: utf-8 -*-
# @Time    : 2019/4/18 下午10:11
# @Author  : Meng Xiao
class Solution:
    def multiply(self, A):
        if not A or len(A) <= 0:
            return
        length = len(A)
        lis = [1] * length
        for i in range(1, length):
            lis[i] = lis[i-1] * A[i-1]
        print(lis)
        temp = 1
        for i in range(length-2, -1, -1):
            temp = temp * A[i+1]
            lis[i] *= temp
        return lis
s = Solution()
print(s.multiply([1,2,3,4]))