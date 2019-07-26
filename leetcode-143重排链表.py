# -*- coding: utf-8 -*-
# @Time    : 2019/7/26 10:53
# @Author  : Meng Xiao
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head):
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return head
        mid = head
        right = head.next
        while right.next and right.next.next:
            mid = mid.next
            right = right.next.next
        right = mid.next
        mid.next = None

        right = self.reverseList(right)

        cur = head
        while cur.next:
            tmp = cur.next
            cur.next = right
            right = right.next
            cur.next.next = tmp
            cur = tmp
        cur.next = right

        return head

    def reverseList(self, head):
        if not head or not head.next:
            return head
        prev = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        return prev
