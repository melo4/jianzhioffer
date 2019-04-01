# -*- coding: utf-8 -*-
# @Time    : 2019/4/1 下午9:15
# @Author  : Meng Xiao
class Solution:
    def reOrderArray(self, array):
        return sorted(array, key=lambda c:c%2, reverse= True )

