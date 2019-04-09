# -*- coding: utf-8 -*-
# @Time    : 2019/4/9 下午3:35
# @Author  : Meng Xiao
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def isSymmetrical(self, pRoot1, pRoot2):
        if pRoot1 == None and pRoot2 == None:
            return True
        if pRoot1 == None or pRoot2 == None:
            return False
        if pRoot1.val != pRoot2.val:
            return False
        return self.isSymmetrical(pRoot1.left, pRoot2.right) and self.isSymmetrical(pRoot1.right, pRoot2.left)
    def selfIsSym(self, pRoot):
        return self.isSymmetrical(pRoot, pRoot)

