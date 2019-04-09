# -*- coding: utf-8 -*-
# @Time    : 2019/3/25 下午4:17
# @Author  : Meng Xiao
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def printListFromTailToHead(self, listNode):
        if not listNode:
            return []
        result = []
        while listNode:
            result.insert(0, listNode.val)
            listNode = listNode.next
        return result
