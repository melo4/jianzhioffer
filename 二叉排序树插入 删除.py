# -*- coding: utf-8 -*-
# @Time    : 2019/8/17 19:03
# @Author  : Meng Xiao
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def InsertBST(self, t, key):
        if not t:
            t = TreeNode(key)
            return t
        if key < t.val:
            t.left = self.InsertBST(t.left, key)
        else:
            t.right = self.InsertBST(t.right, key)
        return t

    def DeleteBST(self, root, key):

        def findmin(root):  # 找到二叉排序树中最小的节点， 即为最左边的节点
            while root.left:
                root = root.left
            return root
        if not root:
            return
        elif key < root.val:
            root.left = self.DeleteBST(root.left, key)
        elif key > root.val:
            root.right = self.DeleteBST(root.right, key)
        
            '''
            如果x没有子节点，或者只有一个孩子，直接将x“切下”;
            否则，x有两个孩子，我们用其右子树中的最小值替换掉x，
            然后将右子树中的这一最小值递归的“切掉”。 ​
            '''
        else:  # root为要删除节点
            if root.left and root.right:
                tmp = findmin(root.right)
                root.val = tmp.val
                root.right = self.DeleteBST(root.right, tmp.val)
            else:
                if not root.left:
                    root = root.right
                elif not root.right:
                    root = root.left
        return root
            
           
            


s = Solution()
t = TreeNode(5)
arr = [5,2,7,1,4]
for x in arr[1:]:
    t = s.InsertBST(t, x)
