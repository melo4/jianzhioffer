# -*- coding: utf-8 -*-
# @Time    : 2019/4/4 下午3:45
# @Author  : Meng Xiao
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 就地逆序
    def reversed1(self, pHead):
        if pHead == None or pHead.next == None:
            return pHead
        pre = None  # 前驱节点
        cur = None  # 当前节点
        next = None  # 后继节点
        cur = pHead.next
        next = cur.next
        cur.next = None
        pre = cur
        cur = next
        # 将当前遍历到的节点cur指向其前驱节点
        while cur.next != None:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        # 最后一个节点指向倒数第二个节点
        cur.next = pre
        pHead.next = cur
        return pHead

    def reversed2(self, pHead):
        # 插入法 从链表第二个节点开始，把遍历到的节点插入到头结点后面
        if pHead is None or pHead.next is None:
            return pHead
        cur = None # 当前节点
        next = None # 后继节点
        cur = pHead.next.next
        pHead.next.next = None
        while cur is not None:
            next = cur.next
            cur.next = pHead.next
            pHead.next = cur
            cur = next

    def reversed3(self, pHead):
        # 递归 不带头结点
        if not pHead or not pHead.next:
            return pHead
        else:
            newHead = self.reversed3(pHead.next)
            pHead.next.next = pHead
            pHead.next = None
        return newHead

    def printLinkList(self, linklist):
        if linklist == None:
            print('None')
            return
        s = ''
        node = linklist.next
        while node != None:
            s = s + str(node.val)
            node = node.next

        print (s)

    def createLinkList(self, linklist_str):
        if len(linklist_str) <= 0:
            return None
        linkList = ListNode(None)
        pNode = linkList
        # 尾插法
        for x in linklist_str:
            node = ListNode(x)

            pNode.next = node
            pNode = pNode.next
        return linkList

s = Solution()
str1 = '123456'
lis = s.createLinkList(str1)
lis1 = s.reversed1(lis)

s.printLinkList(lis1)
