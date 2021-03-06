# -*- coding: utf-8 -*-
# @Time    : 2019/4/4 下午5:22
# @Author  : Meng Xiao
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def HasSubTree(self, pRoot1, pRoot2):
        result = False
        if pRoot1 != None and pRoot2 != None:
            if pRoot1.val == pRoot2.val:
                result = self.DoesTree1haveTree2(pRoot1, pRoot2)
            if not result:
                result = self.HasSubTree(pRoot1.left, pRoot2)
            if not result:
                result = self.HasSubTree(pRoot1.right, pRoot2)
        return result


    def DoesTree1haveTree2(self, pRoot1, pRoot2):
        if pRoot2 == None:
            return False
        if pRoot1 == None:
            return False
        if pRoot1.val != pRoot2.val:
            return False
        return self.DoesTree1haveTree2(pRoot1.left, pRoot2.left) and self.DoesTree1haveTree2(pRoot1.right, pRoot2.right)
