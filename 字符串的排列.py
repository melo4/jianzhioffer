# -*- coding: utf-8 -*-
# @Time    : 2019/4/11 下午8:56
# @Author  : Meng Xiao
class Solution:

    # 全排列
    def Permutation(self, ss):
        if not ss:
            return []
        if len(ss) == 1:
            return list(ss)
        charlist = list(ss)
        charlist.sort()
        res = []
        for i in range(len(charlist)):
            if i > 0 and charlist[i] == charlist[i-1]:
                continue
            temp = self.Permutation(''.join(charlist[:i])+''.join(charlist[i+1:]))
            for j in temp:
                res.append(charlist[i] + j)

        return res

    # 全组合
    def Combination(self, ss):
        # 由于全组合含有空集，这里结果采用列表形式
        if not ss:
            return []
        res = [[]]
        charlist = list(ss)
        for i in charlist:
            for j in range(len(res)):
                res.append(res[j]+[i])
        return res
s = Solution()
print(s.Permutation('111324'))