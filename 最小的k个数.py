# -*- coding: utf-8 -*-
# @Time    : 2019/4/13 下午2:32
# @Author  : Meng Xiao
'''
快速排序取前K个
'''
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        if not tinput or k > len(tinput):
            return []
        tinput = self.quick_sort(tinput)
        return tinput[:k]

    def quick_sort(self, lst):
        if not lst:
            return []
        pivot = lst[0]
        left = self.quick_sort([x for x in lst[1:] if x < pivot])
        right = self.quick_sort([x for x in lst[1:] if x >= pivot])

        return left + [pivot] + right

'''
方法2 堆
'''
def getleastnums(array, k):
    import heapq
    max_heap = []
    for x in array:
        heapq.heappush(max_heap, -x)
        if len(max_heap) > k:
            heapq.heappop(max_heap)
    for x in max_heap:
        print(-x, end=' ')
    print()
