# -*- coding: utf-8 -*-
# @Time    : 2019/4/9 下午9:16
# @Author  : Meng Xiao
class Solution:
    def IsPopOrder(self, pushV, popV):
        if pushV == [] or popV == []:
            return False
        stack = []  # 辅助栈
        for i in pushV:
            stack.append(i)
            while len(stack) and stack[-1] == popV[0]:
                stack.pop()
                popV.pop(0)
        if len(stack):
            return False
        else:
            return True