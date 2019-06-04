# -*- coding: utf-8 -*-
# @Time    : 2019/6/4 20:17
# @Author  : Meng Xiao
'''
给定一个链表，翻转该链表从m到n的位置。要求直接翻转而非申请新空间。
如：给定1→2→3→4→5，m=2，n=4，返回1→4→3→2→5。
假定给出的参数满足：1≤m≤n≤链表长度。
'''

class ListNode:
    val = None
    next = None

# 创建带头结点的链表
def createLinkList(linklist_str):
    if len(linklist_str) <= 0:
        return None
    linkList = ListNode()
    pNode = linkList
    # 尾插法
    for x in linklist_str:
        node = ListNode()
        node.val = x
        pNode.next = node
        pNode = pNode.next
    return linkList

# 打印链表
def printLinkList(linklist):
    if linklist == None:
        print('None')
        return
    s = ''
    node = linklist.next
    while node != None:
        s = s + str(node.val)
        node = node.next
    print(s)

# 翻转链表从m到n位置
def reverseLinkList(linklist, m, n):
    '''
    先找到第m个元素， 然后把链表中的第n个元素添加到它前面，重复执行n-m次
    '''
    # 找到第m个节点的前个节点
    preMNode = linklist
    for i in range(m-1):
        preMNode = preMNode.next

    for i in range(n-m):
        preNNode = linklist
        # 找到第n个节点的前节点
        for j in range(n-1):
            preNNode = preNNode.next
        nNode = preNNode.next #第n个节点
        preNNode.next = preNNode.next.next
        nNode.next = preMNode.next
        preMNode.next = nNode
        preMNode = preMNode.next
        printLinkList(linklist)

if __name__ == '__main__':
    s = '123456'
    linklist = createLinkList(s)
    printLinkList(linklist)
    reverseLinkList(linklist,2,5)