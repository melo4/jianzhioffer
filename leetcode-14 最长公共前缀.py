# -*- coding: utf-8 -*-
# @Time    : 2019/5/14 22:02
# @Author  : Meng Xiao

class Solution(object):
    '''
    首先 ，最长公共前缀，长度不可能大于strs[0],只要strs中存在比当前长度i更短的string，
    立刻返回上一轮LCP，即strs[0][:i]
只要strs中存在当前index字符与LCP该index不相同的字符串，立刻返回上一轮LCP，即strs[0][:i]
如果一直没返回，说明strs[0]本身就是LCP，返回它
    '''
    def longestCommonPrefix(self, strs):

        if not strs:
            return ''
        for i in range(len(strs[0])):
            for str in strs:
                if len(str) <= i or strs[0][i] != str[i]:
                    return strs[0][:i]
        return strs[0]