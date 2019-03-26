# -*- coding: utf-8 -*-
# @Time    : 2019/3/25 下午5:35
# @Author  : Meng Xiao
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None
class Solution:
    def GetNext(self, pNode):
        if pNode is None:
            return
        pNext = None
        if pNode.right:
            pNext = pNode.right
            while pNode.left:
                pNode = pNode.left
            pNext = pNode
        else:
            if pNode.next and pNode.next.left == pNode:
                pNext = pNode.next
            elif pNode.next and pNode.next.right == pNode:
                pNode = pNode.next
                while pNode.next and pNode.next.right == pNode:
                    pNode = pNode.next
                if pNode.next:
                    pNext = pNode.next
        return pNext

