# -*- coding: utf-8 -*-
# @Time    : 2019/4/15 下午9:33
# @Author  : Meng Xiao
class Solution:
    '''
    动态规划，f(i):以第i个字符结尾的字符串包含不包含重复字符的子串长度
    '''
    def longestSub(self, s):
        if not s:
            return
        curLength = 0
        maxLength = 0
        position = [-1] * 26 #用于标示每个字符上次出现的位置
        for i in range(len(s)):
            preIndex = position[ord(s[i])-ord('a')]
            if preIndex < 0 or i - preIndex > curLength:
                curLength += 1
            else:
                if curLength > maxLength:
                    maxLength = curLength
                curLength = i - preIndex
            position[ord(s[i])-ord('a')] = i
        # if curLength > maxLength:
        #     maxLength = curLength
        return maxLength

s = Solution()
print(s.longestSub('arabcacfr'))