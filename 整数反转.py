# -*- coding: utf-8 -*-
# @Time    : 2019/5/7 20:54
# @Author  : Meng Xiao
class Solution(object):
    def reverse(self, x):

        if x < 0:
            return -self.reverse(-x)
        res = 0
        while x:
            res = res * 10 + x % 10
            x /= 10
        return res if res <= 0x7fffffff else 0