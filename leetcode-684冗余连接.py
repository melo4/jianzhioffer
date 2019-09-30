# -*- coding: utf-8 -*-
# @Time    : 2019/9/30 17:26
# @Author  : Meng Xiao
class Solution:
    def findRedundantConnection(self, edges):

        p = {i: {i} for i in range(1, len(edges) + 1)}  # 并查集初始化
        for x, y in edges:
            if p[x] is not p[y]:  # 如果两个集合地址不一样
                p[x] |= p[y]  # 合并集合
                for z in p[y]:
                    p[z] = p[x]  # 修改元素集合标记的指针地址
            else:
                return [x, y]

