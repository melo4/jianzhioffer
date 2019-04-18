# -*- coding: utf-8 -*-
# @Time    : 2019/4/18 下午9:06
# @Author  : Meng Xiao
class Solution:
    def maxInWindows(self, num, size):
        if not num or size <= 0:
            return []
        if len(num) <= size:
            return [max(num)]
        deque = []
        index = []
        for i in range(size):
            while len(index) > 0 and num[i] > num[index[-1]]:
                index.pop()
            index.append(i)
        for i in range(size, len(num)):
            deque.append(num[index[0]])
            while len(index) > 0 and num[i] >= num[index[-1]]:
                index.pop()
            if len(index) > 0 and index[0] <= i - size:
                index.pop(0)
            index.append(i)
        deque.append(num[index[0]])
        return deque
s = Solution()
print(s.maxInWindows([2,3,4,2,6,2,5,1],3))

