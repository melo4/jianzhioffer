# -*- coding: utf-8 -*-
# @Time    : 2019/4/22 下午10:05
# @Author  : Meng Xiao
class Solution:
    def findMaxDivision(self, alist):
        if not alist:
            return
        length = len(alist)
        if length < 2:
            return 0
        maxnum = max(alist)
        minnum = min(alist)
        bucket = [0] * (maxnum-minnum+1) # 生成桶
        for i in range(length):
            bucket[alist[i]-minnum] += 1
        count = 0
        maxD = 0
        for i in range(len(bucket)):
            if bucket[i] == 0:
                count += 1
            else:
                if maxD < count:
                    maxD = count
                count = 0
        return maxD + 1
s = Solution()
print(s.findMaxDivision([1,1]))