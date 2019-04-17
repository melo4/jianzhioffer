# -*- coding: utf-8 -*-
# @Time    : 2019/4/17 下午3:46
# @Author  : Meng Xiao
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def inorderTraversal1(self, root):
        if not root:
            return []
        return self.inorderTraversal1(root.left) + [root.val] + self.inorderTraversal1(root.right)

    def inorderTraversal2(self, root):
        '''
        规律：当curnode不为None时，每一次循环将curnode入栈，如果curnode不为None,则出栈一个节点并加入res
        '''
        if not root:
            return []
        stack = []
        res = []
        curnode = root
        while stack or curnode:
            if curnode:
                stack.append(curnode)
                curnode = curnode.left
            else:
                curnode = stack.pop()
                res.append(curnode.val)
                curnode = curnode.right
        return res

    def preorderTraversal1(self, root):
        if not root:
            return []
        return [root.val] + self.preorderTraversal1(root.left) + self.preorderTraversal1(root.right)

    def preorderTraversal2(self, root):
        if not root:
            return []
        curnode = root
        stack = []
        res = []
        while stack or curnode:
            if curnode:
                res.append(curnode.val)
                stack.append(curnode.right)
                curnode = curnode.left
            else:
                curnode = stack.pop()
        return res

    def postorderTraversal1(self, root):
        if not root:
            return []
        return self.postorderTraversal1(root.left) + self.postorderTraversal1(root.right) + [root.val]

    def postorderTraversal2(self, root):
        if not root:
            return []
        curnode = root
        stack = []
        res = []
        while stack or curnode:
            if curnode:
                res.append(curnode.val)
                stack.append(curnode.left)
                curnode = curnode.right
            else:
                curnode = stack.pop()
        return res[::-1]

    '''
    层序遍历，也叫宽度优先遍历。
    '''
    def levelorderTraversal1(self, root):
        # 递归学要一个参数level ,表示当前节点的层数。
        def helper(node, level):
            if not node:
                return
            else:
                res[level-1].append(node.val)
                if len(res) == level:
                    res.append([])
                helper(node.left, level+1)
                helper(node.right, level+1)
        res = [[]]
        helper(root, 1)
        return res[:-1]

    def levelorderTraversal2(self, root):
        if not root:
            return []
        res = []
        curnode = root
        queue = [curnode]
        while queue:
            curnode = queue.pop(0)
            res.append(curnode.val)
            if curnode.left:
                queue.append(curnode.left)
            if curnode.right:
                queue.append(curnode.right)
        return res


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

print(s.levelorderTraversal1(a))
print(s.levelorderTraversal2(a))
