# -*- coding: utf-8 -*-
# @Time    : 2019/4/4 下午4:16
# @Author  : Meng Xiao
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def Merge(self, pHead1, pHead2):
        if pHead1 == None:
            return pHead2
        if pHead2 == None:
            return pHead1

        if pHead1.val < pHead2.val:
            pMergeHead = pHead1
            pMergeHead.next = self.Merge(pHead1.next, pHead2)
        else:
            pMergeHead = pHead2
            pMergeHead.next = self.Merge(pHead1, pHead2.next)
        return pMergeHead