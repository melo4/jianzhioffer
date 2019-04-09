# -*- coding: utf-8 -*-
# @Time    : 2019/4/9 下午8:49
# @Author  : Meng Xiao
class Solution:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, node):
        self.stack.append(node)
        if self.minStack == [] or node < self.min():
            self.minStack.append(node)
        else:
            tmp = self.min()
            self.minStack.append(tmp)

    def pop(self):
        if self.stack == None or self.minStack == None:
            return None
        self.minStack.pop()
        self.stack.pop()
    def min(self):
        return self.minStack[-1]
