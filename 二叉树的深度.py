# -*- coding: utf-8 -*-
# @Time    : 2019/4/17 下午8:50
# @Author  : Meng Xiao
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    '''
    递归
    '''
    def TreeDepth(self, root):
        if not root:
            return 0
        return max(self.TreeDepth(root.left), self.TreeDepth(root.right)) + 1
    '''
    非递归
    '''
    def TreeDepth1(self, root):
        if not root:
            return 0
        queue = []
        queue.append((root, 1))
        while queue:
            curnode, depth = queue.pop(0)
            if curnode.left:
                queue.append((curnode.left, depth+1))
            if curnode.right:
                queue.append((curnode.right, depth+1))
        return depth

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

print(s.TreeDepth1(a))
