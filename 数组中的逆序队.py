# -*- coding: utf-8 -*-
# @Time    : 2019/4/16 下午4:44
# @Author  : Meng Xiao
count = 0
class Solution:
    def InversePairs(self, data):
        count = 0
        for item in (sorted(data)):
            count += data.index(item)
            data.remove(item)
        return count

    # 归并排序思想
    def InversePairs1(self, data):
        global count
        def MergeSort(lists):
            global count
            if len(lists) <= 1:
                return lists
            num = len(lists) // 2
            left = MergeSort(lists[:num])
            right = MergeSort(lists[num:])
            i, j = 0, 0
            result = []
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1
                    count += len(left) - i

            result += right[j:]
            result += left[i:]
            return result
        MergeSort(data)
        return count

s = Solution()
print(s.InversePairs1([7,5,6,4]))

