# -*- coding: utf-8 -*-
# @Time    : 2019/8/12 10:32
# @Author  : Meng Xiao

'''
链表的nlogn排序
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergesort(self, head):
        #归并排序
        if head == None or head.next == None:
            return head
        mid = self.findMid(head)
        l1 = head  # split
        l2 = mid.next
        mid.next = None
        l1 = self.mergesort(l1)
        l2 = self.mergesort(l2)
        return  self.mergeTwoLists(l1, l2)

    def mergeTwoLists(self, l1, l2):
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        dummy = ListNode(-1)
        cur = dummy
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        if l1: # 兜底
            cur.next = l1
        else:
            cur.next = l2
        return dummy.next

    def findMid(self, head):
        if head == None or head.next == None:
            return head
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    '''
    快速排序
    '''
    def quickSort(self, head):
        if head == None or head.next == None:
            return head
        leftH = ListNode(-1)
        resL = leftH
        rightH = ListNode(-1)
        resR = rightH
        pivotNode = head  # pivot
        cur = head.next
        while cur != None:
            if cur.val < pivotNode.val:
                leftH.next = cur
                leftH = leftH.next
            else:
                rightH.next = cur
                rightH = rightH.next
            cur = cur.next
        leftH.next = None
        rightH.next = None
        L = self.quickSort(resL.next)
        R = self.quickSort(resR.next)
        pivotNode.next = R
        if L == None:
            return pivotNode
        tmp = L
        while tmp.next != None:
            tmp = tmp.next
        tmp.next = pivotNode
        return L

