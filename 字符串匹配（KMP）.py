# -*- coding: utf-8 -*-
# @Time    : 2019/7/9 20:41
# @Author  : Meng Xiao

class Solution:
    def violent_match(self, s, p):
        #暴力匹配法
        sLen = len(s)
        pLen = len(p)
        i = 0
        j = 0
        while i < sLen and j < pLen:
            if s[i] == p[j]:
                i += 1
                j += 1

            else:
                i = i - j + 1 # i-(j-1)
                j = 0
        if j == pLen:
            return i - j
        else:
            return -1

    def kmp_match(self, s, p):
        i, j = 0, 0
        sLen, pLen = len(s), len(p)
        next = self.get_next_p(p)
        print(next)
        while i < sLen and j < pLen:
            if j == -1 or s[i] == p[j]:
                i += 1
                j += 1
            else:
                j = next[j]
        if j == pLen:
            return i - j
        else:
            return -1

    def get_next(self, p):
        # 递推方式求next数组(未优化版本)
        pLen = len(p)
        next = [-1] * pLen
        k = -1
        j = 0
        while j < pLen - 1:
            if k == -1 or p[j] == p[k]:
                k += 1
                j += 1
                next[j] = k
            else:
                k = next[k]
        return next
    def get_next_p(self, p):
        # 优化版本， 即p[j]不能等于next[j]
        pLen = len(p)
        next = [-1] * pLen
        k = -1
        j = 0
        while j < pLen - 1:
            if k == -1 or p[j] == p[k]:
                j += 1
                k += 1
                if p[j] != p[k]:
                    next[j] = k
                else:
                    #因为不能出现p[j] = p[next[j]]，所以当出现时需要继续递归，
                    # k = next[k] = next[next[k]]
                    next[j] = next[k]
            else:
                k = next[k]
        return next

