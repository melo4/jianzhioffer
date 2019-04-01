# -*- coding: utf-8 -*-
# @Time    : 2019/4/1 下午7:31
# @Author  : Meng Xiao
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def deleteDuplication(self, pHead):
        if pHead is None or pHead.next is None:
            return pHead
        first = ListNode(-1)
        first.next = pHead
        last = first
        while pHead and pHead.next:
            if pHead.val == pHead.next.val:
                val = pHead.val
                while pHead and val == pHead.val:
                    pHead = pHead.next
                last.next = pHead
            else:
                last = pHead
                pHead = pHead.next

        return first.next