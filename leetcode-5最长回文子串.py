# -*- coding: utf-8 -*-
# @Time    : 2019/5/7 19:32
# @Author  : Meng Xiao
class Solution:
# 法1 ： 依次把每个字符作为回文字符串的中间字符。
    def longestPalindrome1(self, s):
        n = len(s)
        maxLength = 0
        left = right = 0
        for i in range(n):
            # 长度为奇数情况：
            for j in range(min(i+1, n-i)):
                if s[i-j] != s[i+j]:
                    break
                if 2 * j + 1 > maxLength:
                    maxLength = 2 * j + 1
                    left = i - j
                    right = i + j
            # 偶数
            if i + 1 < n and s[i] == s[i+1]:
                for j in range(min(i+1, n-i-1)):
                    if s[i-j] != s[i+1+j]:
                        break
                    if 2 * j + 2 > maxLength:
                        maxLength = 2 * j + 2
                        left = i - j
                        right = i + j + 1
        return s[left:right+1]

    # 法2：Manacher算法.https://www.felix021.com/blog/read.php?2040
    def longestPalindrome2(self, s):
        def preProcess(s):
            if not s:
                return ['^', '$']
            T = ['^']
            for i in s:
                T += ['#', i]
            T += ['#', '$']
            return T
        T = preProcess(s)
        P = [0] * len(T) # P[i]表示以s[i]为回文串中心时，此回文串的长度
        id, mx = 0, 0 # id表示最大回文串中心的位置，mx则为id+P[id],即最大回文串的右边界
        for i in range(1, len(T)-1):
            j = 2 * id - i # j为i关于id的对称位置
            if mx > i:
                P[i] = min(P[j], mx-i)
            else:
                P[i] = 0
            while T[i+P[i]+1] == T[i-P[i]-1]:
                P[i] += 1
            if i + P[i] > mx:
                id, mx = i, i + P[i]
        max_i = P.index(max(P))
        start = (max_i - P[max_i] - 1) // 2
        res = s[start:start+P[max_i]]
        return res


s = Solution()
print(s.longestPalindrome2('babad'))