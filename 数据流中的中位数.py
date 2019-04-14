# -*- coding: utf-8 -*-
# @Time    : 2019/4/13 下午4:07
# @Author  : Meng Xiao
class Solution:
    def __init__(self):
        self.left = []
        self.right = []
        self.count = 0

    def Insert(self, num):
        if self.count & 1 == 0:
            self.left.append(num)
        else:
            self.right.append(num)
        self.count += 1

    def getMedian(self,x ):
        if self.count == 1:
            return self.left[0]
        self.MaxHeap(self.left)
        self.MinHeap(self.right)
        if self.left[0] > self.right[0]:
            self.left[0], self.right[0] = self.right[0], self.left[0]
        self.MaxHeap(self.left)
        self.MinHeap(self.right)
        if self.count & 1 == 0:
            return (self.left[0] + self.right[0]) / 2.0
        else:
            return self.left[0]

    def MaxHeap(self, alist):
        import heapq
        max_heap = []
        for i in alist:
            heapq.heappush(max_heap, -i)
        return [-heapq.heappop(max_heap) for i in range(len(alist))]

    def MinHeap(self, alist):
        import heapq
        max_heap = []
        for i in alist:
            heapq.heappush(max_heap, i)
        return [heapq.heappop(max_heap) for i in range(len(alist))]
