# -*- coding: utf-8 -*-
# @Time    : 2019/4/11 下午8:14
# @Author  : Meng Xiao
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def __init__(self):
        self.flag = -1
    def Serialize(self, root):
        if not root:
            return '$,'
        return str(root.val)+','+self.Serialize(root.left)+self.Serialize(root.right)

    def Deserialize(self, s):

        self.flag += 1
        l = s.split(',')

        if self.flag >= len(s):
            return None
        root = None

        if l[self.flag] != '$':
            root = TreeNode(int(l[self.flag]))
            root.left = self.Deserialize(s)
            root.right = self.Deserialize(s)
        return root
