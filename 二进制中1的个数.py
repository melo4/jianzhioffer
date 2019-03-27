# -*- coding: utf-8 -*-
# @Time    : 2019/3/27 下午9:33
# @Author  : Meng Xiao

class Solution:
    def Numberof1(self, n):
        count = 0
        if n < 0:
            n = n & 0xffffffff
        while n != 0:
            count += 1
            n = (n - 1) & n
        return count
