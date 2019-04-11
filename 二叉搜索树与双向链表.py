# -*- coding: utf-8 -*-
# @Time    : 2019/4/11 下午7:44
# @Author  : Meng Xiao
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def Convert(self, pRoot):
        if not pRoot:
            return None
        if not pRoot.left and pRoot.right:
            return pRoot

        self.Convert(pRoot.left)
        left = pRoot.left

        if left:
            while left.right:
                left = left.right
            pRoot.left = left
            left.right = pRoot

        self.Convert(pRoot.right)
        right = pRoot.right

        if right:
            while right.left:
                right = right.left
            pRoot.right = right
            right.left = pRoot

        while pRoot.left:
            pRoot = pRoot.left

        return pRoot

