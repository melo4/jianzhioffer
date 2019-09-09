# -*- coding: utf-8 -*-
# @Time    : 2019/8/31 21:35
# @Author  : Meng Xiao

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.global_max = root.val if root else 0
        self.findmax(root)
        return self.global_max

    def findmax(self, node):
        if not node:
            return 0
        left = self.findmax(node.left)
        left = left if left > 0 else 0
        right = self.findmax(node.right)
        right = right if right > 0 else 0
        self.global_max = max(node.val + left + right, self.global_max)

        return max(left, right) + node.val