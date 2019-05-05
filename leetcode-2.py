# -*- coding: utf-8 -*-
# @Time    : 2019/5/5 20:46
# @Author  : Meng Xiao

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    def addTwoNumbers(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1
        cur = head = ListNode(-1)
        carry = 0
        while l1 and l2:
            value = (l1.val + l2.val + carry) % 10
            carry = (l1.val + l2.val + carry) // 10
            cur.next = ListNode(value)
            cur = cur.next
            l1 = l1.next
            l2 = l2.next
        rest = l1 or l2
        while rest:
            value = (rest.val + carry) % 10
            cur.next = ListNode(value)
            carry = (rest.val + carry) // 10
            cur = cur.next
            rest = rest.next
        if carry:
            cur.next = ListNode(1)
        return head.next
