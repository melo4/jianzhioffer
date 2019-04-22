# -*- coding: utf-8 -*-
# @Time    : 2019/4/22 下午4:12
# @Author  : Meng Xiao
class Solution:
    def maxSubSequence(self, s1, s2):
        if not s1 or not s2:
            return
        if len(s1) == 0 or len(s2) == 0:
            return 0
        flag = 0
        dp = [[0 for j in range(len(s2)+1)] for i in range(len(s1)+1)]
        for i in range(1, len(s1)+1):
            for j in range(1, len(s2)+1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        i, j = len(s1), len(s2)
        while i >= 1 and j >= 1:
            if s1[i-1] == s2[j-1]:
                print(s1[i-1])
                i -= 1
                j -= 1
            else:
                if dp[i][j-1] > dp[i-1][j]:
                    j -= 1
                else:
                    i -= 1

        return dp[-1][-1]

    # 最长公共子串
    def maxSubStr(self, s1, s2):
        if not s1 or not s2:
            return
        len1 = len(s1)
        len2 = len(s2)
        dp = [[0 for j in range(len2)] for i in range(len1)]
        maxLength = 0
        for i in range(len1):
            for j in range(len2):
                if s1[i] == s2[j]:
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = dp[i-1][j-1] + 1
                    if dp[i][j] > maxLength:
                        maxLength = dp[i][j]
                        start_index = i - dp[i][j] + 1
        print(s1[start_index:start_index+maxLength])
        return maxLength


s = Solution()
print(s.maxSubStr('BDCABA','ABCBDAB'))
