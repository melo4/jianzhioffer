# -*- coding: utf-8 -*-
# @Time    : 2019/6/24 19:56
# @Author  : Meng Xiao

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 用二分的思想，就是把 Lists 分为两部分，
    # 分别递归 Merge k Sorted Lists 后变成两个 List ，
    # 然后再对这两 List 进行 Merge Two Sorted Lists 。
    def mergeKLists(self, lists):
        # lists: List[ListNode]) -> ListNode:
        if len(lists) == 0:
            return
        if len(lists) == 1:
            return lists[0]

        mid = len(lists) // 2
        left = self.mergeKLists(lists[:mid])
        right = self.mergeKLists(lists[mid:])

        # merge left and right
        dummy = ListNode(-1)
        cur = dummy
        while left or right:
            if right == None or (left and left.val <= right.val):
                cur.next = left
                left = left.next
            else:
                cur.next = right
                right = right.next
            cur = cur.next
        return dummy.next

    # 使用堆优先队列
    def mergeKListq(self, lists):
        import heapq
        heap = []
        p = dummy = ListNode(-1)
        for i in range(len(lists)):
            node = lists[i]
            if not node:
                continue
            heapq.heappush(heap, (node.val, node))
        while heap:
            value, node = heapq.heappop(heap)
            p.next = node
            p = p.next
            if node.next:
                node = node.next
                heapq.heappush(heap, (node.val, node))
        return dummy.next