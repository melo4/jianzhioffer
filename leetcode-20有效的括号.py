# -*- coding: utf-8 -*-
# @Time    : 2019/6/17 20:39
# @Author  : Meng Xiao
class Solution:
    def isValid(self, s):
        mp = {')': '(', ']': '[', '}': '{'}
        stk = []
        for ch in s:
            if ch in '([{':
                stk.append(ch)
            else:
                if not stk or mp[ch] != stk.pop():
                    return False
        return not stk