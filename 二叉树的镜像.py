# -*- coding: utf-8 -*-
# @Time    : 2019/4/9 下午2:52
# @Author  : Meng Xiao
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def mirrorRecursively(self, pRoot):
        if pRoot is None:
            return
        if pRoot.left is None and pRoot.right is None:
            return pRoot
        pTemp = pRoot.left
        pRoot.left = pRoot.right
        pRoot.right = pTemp

        self.mirrorRecursively(pRoot.left)
        self.mirrorRecursively(pRoot.right)
        return pRoot

    def printTree(self, pRoot):
        if pRoot is None:
            return
        print(pRoot.val)
        self.printTree(pRoot.left)
        self.printTree(pRoot.right)
a = TreeNode(8)
b = TreeNode(6)
c = TreeNode(10)
d = TreeNode(5)
e = TreeNode(7)
f = TreeNode(9)
g = TreeNode(11)
a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
c.right = g

s = Solution()
print(s.printTree(a))
s.mirrorRecursively(a)
print(s.printTree(a))