# -*- coding: utf-8 -*-
# @Time    : 2019/4/16 下午4:33
# @Author  : Meng Xiao
class Solution:
    def __init__(self):
        self.dic = {}
        self.lis = []

    def FirstAppearingOnce(self):
        while len(self.lis) > 0 and self.dic[self.lis[0]] == 2:
            self.lis.pop(0)
        if len(self.lis) == 0:
            return '#'
        else:
            return self.lis[0]

    def Insert(self, char):
        if char not in self.dic.keys():
            self.dic[char] = 1
            self.lis.append(char)
        elif self.dic[char]:
            self.dic[char] = 2