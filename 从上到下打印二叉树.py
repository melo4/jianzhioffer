# -*- coding: utf-8 -*-
# @Time    : 2019/4/10 下午5:16
# @Author  : Meng Xiao
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def PrintFromTopToBottom(self, root):
        if root is None:
            return []
        queue = []  # 临时队列
        result = []     # 结果

        queue.append(root)
        while(len(queue)) > 0:
            currentRoot = queue.pop(0)
            result.append(currentRoot.val)
            if currentRoot.left:
                queue.append(currentRoot.left)
            if currentRoot.right:
                queue.append(currentRoot.right)
        return result