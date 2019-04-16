# -*- coding: utf-8 -*-
# @Time    : 2019/4/16 下午4:02
# @Author  : Meng Xiao
class Solution:
    def FirstNotRepeatingChar(self, s):
        if not s:
            return
        store = {}
        lis = list(s)
        for i in lis:
            if i not in store.keys():
                store[i] = 0
            store[i] += 1
        for i in lis:
            if store[i] == 1:
                return i
        return
