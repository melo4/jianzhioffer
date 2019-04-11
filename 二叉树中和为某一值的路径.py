# -*- coding: utf-8 -*-
# @Time    : 2019/4/11 下午3:27
# @Author  : Meng Xiao
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNum):
        if not root or root.val > expectNum:
            return []
        if not root.left and not root.right and root.val == expectNum:
            return [[root.val]]
        else:
            expectNum -= root.val
            left = self.FindPath(root.left, expectNum)
            right = self.FindPath(root.right, expectNum)

            result = [[root.val]+i for i in left]
            for i in right:
                result.append([root.val]+i)

        return result
a = TreeNode(10)
b = TreeNode(5)
c = TreeNode(12)
d = TreeNode(4)
e = TreeNode(7)
a.left = b
a.right = c
b.left = d
b.right = e
s = Solution()
print(s.FindPath(a, 22))
