# -*- coding: utf-8 -*-
# @Time    : 2019/3/27 下午9:15
# @Author  : Meng Xiao
class Solution:
    def cutRecursion(self, length):
        if length < 2:
            return 0
        if length == 2:
            return 1
        if length == 3:
            return 2
        products = [0, 1, 2, 3]

        max = 0
        for i in range(4, length+1):
            products.append(None)
            max = 0
            for j in range(1, i//2+1):
                product = products[j] * products[i-j]
                if max < product:
                    max = product
                products[i] = max

        return products[length]

