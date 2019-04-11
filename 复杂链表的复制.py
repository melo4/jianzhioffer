# -*- coding: utf-8 -*-
# @Time    : 2019/4/11 下午4:21
# @Author  : Meng Xiao
class RandomListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.random = None
class Solution:
    def Clone(self, pHead):
        if not pHead:
            return None
        pNode = pHead
        while pNode:
            pClone = RandomListNode(pNode.val)
            pClone.next = pNode.next
            pNode.next = pClone
            pNode = pClone.next

        pNode = pHead
        while pNode:
            pClone = pNode.next
            if pNode.random != None:
                pClone.random = pNode.random.next
            pNode = pClone.next

        pNode = pHead
        pCloneHead = pCloneNode = pNode.next
        pNode.next = pCloneHead.next
        pNode = pNode.next

        while pNode:
            pCloneNode.next = pNode.next
            pCloneNode = pCloneNode.next
            pNode.next = pCloneNode.next
            pNode = pNode.next
        return pCloneHead