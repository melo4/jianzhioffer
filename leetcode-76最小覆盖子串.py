# -*- coding: utf-8 -*-
# @Time    : 2019/8/21 上午12:23
# @Author  : Meng Xiao
import collections
class Solution:
    def minWindow(self, s, t):
        if len(s) < len(t):
            return ''
        maps = collections.Counter(t)
        counter = len(maps)
        begin, end, head, length = 0, 0, 0, float('inf')
        while end < len(s):
            if s[end] in maps:
                maps[s[end]] -= 1
                if maps[s[end]] == 0:
                    counter -= 1
            end += 1
            while counter == 0:
                if s[begin] in maps:
                    maps[s[begin]] += 1
                    if maps[s[begin]] > 0:
                        counter += 1
                if end - begin < length:
                    length = end - begin
                    head = begin
                begin += 1
        if length == float('inf'):
            return ''
        return s[head:head+length-1]
