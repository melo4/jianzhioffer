# -*- coding: utf-8 -*-
# @Time    : 2019/4/16 下午7:23
# @Author  : Meng Xiao
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        if not pHead1 or not pHead2:
            return None
        p1, p2 = pHead1, pHead2
        len1 = len2 = 0
        while p1:
            len1 += 1
            p1 = p1.next
        while p2:
            len2 += 1
            p2 = p2.next
        if len1 > len2:
            while len1 - len2:
                pHead1 = pHead1.next
                len1 -= 1
        else:
            while len2 - len1:
                pHead2 = pHead2.next
                len2 -= 1
        while pHead1 and pHead2:
            if pHead1 is pHead2:
                return pHead1
            pHead2 = pHead2.next
            pHead1 = pHead1.next

        return None
