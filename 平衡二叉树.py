# -*- coding: utf-8 -*-
# @Time    : 2019/4/17 下午9:20
# @Author  : Meng Xiao
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def __init__(self):
        self.flag = True

    def isBalanced(self, root):
        self.getDepth(root)
        return self.flag

    def getDepth(self, root):
        if not root:
            return 0
        left = self.getDepth(root.left) + 1
        right = self.getDepth(root.right) + 1
        if abs(left - right) > 1:
            self.flag = False
        return max(left, right)

s = Solution()
a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)
f = TreeNode(6)
g = TreeNode(7)
a.left = b
a.right = c
b.left = d
b.right = e
c.right = f
e.left = g

print(s.isBalanced(a))
