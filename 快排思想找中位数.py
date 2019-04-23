# -*- coding: utf-8 -*-
# @Time    : 2019/4/23 下午5:28
# @Author  : Meng Xiao

class Solution:

    def midNumber(self, alist, left, right):
        if left >= right:
            return alist[left]
        key = alist[left]
        low = left
        high = right
        mid = (len(alist) - 1) // 2
        while left < right:
            while left < right and alist[right] >= key:
                right -= 1
            alist[left] = alist[right]
            while left < right and alist[left] <= key:
                left += 1
            alist[right] = alist[left]
        alist[right] = key
        if right == mid:

            return key
        elif right < mid:

            return self.midNumber(alist, left+1, high)
        else:
            return self.midNumber(alist, low, left-1)

s = Solution()
output = s.midNumber([1,1,1,3,5,4,6], 0, 6)
print(output)

