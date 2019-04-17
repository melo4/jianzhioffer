# -*- coding: utf-8 -*-
# @Time    : 2019/4/17 下午3:15
# @Author  : Meng Xiao
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def KthNode(self, pRoot, k):
        if pRoot is None or not k:
            return
        res = []
        def traverse(node):
            if len(res) >= k or not node:
                return
            traverse(node.left)
            res.append(node)
            traverse(node.right)
        traverse(pRoot)
        if len(res) < k:
            return
        return res[k-1]