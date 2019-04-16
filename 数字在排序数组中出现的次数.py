# -*- coding: utf-8 -*-
# @Time    : 2019/4/16 下午9:55
# @Author  : Meng Xiao
class Solution:

    def GetNumberOfK(self, data, k):
        if not data:
            return 0
        if self.GetFirstK(data, k) == -1 and self.GetLastK(data, k) == -1:
            return 0
        return self.GetLastK(data, k) - self.GetFirstK(data, k) + 1

    def GetFirstK(self, data, k):
        low = 0
        high = len(data) - 1
        while low <= high:
            mid = (low+high) // 2
            if data[mid] < k:
                low = mid + 1
            elif data[mid] > k:
                high = mid - 1
            else:
                if mid == low or data[mid-1] != k:
                    return mid
                else:
                    high = mid - 1
        return -1

    def GetLastK(self, data, k):
        low = 0
        high = len(data) - 1
        while low <= high:
            mid = (low + high) // 2
            if data[mid] < k:
                low = mid + 1
            elif data[mid] > k:
                high = mid - 1
            else:
                if mid == high or data[mid + 1] != k:
                    return mid
                else:
                    low = mid + 1
        return -1

s = Solution()
print(s.GetNumberOfK([1,2,3,3,3,3,4,5],3))