# -*- coding: utf-8 -*-
# @Time    : 2019/4/4 上午10:16
# @Author  : Meng Xiao
'''
动态规划思想：dp[i][j]表示将字符串A[0:i-1]转变为B[0:j-1]的最小步骤数
'''

class Solution:
    def editDistance(self, str1, str2):
        n1, n2 = len(str1), len(str2)
        if n1 == 0:
            return n2
        if n2 == 0:
            return n1
        edit = [[i + j for j in range(n2 + 1)] for i in range(n1 + 1)] # 初始化边界

        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if str1[i-1] == str2[j-1]:
                    d = 0
                else:
                    d = 1
                edit[i][j] = min(edit[i-1][j]+1, edit[i][j-1]+1, edit[i-1][j-1]+d)
        return edit#

s = Solution()
print(s.editDistance('abcf', 'abde'))