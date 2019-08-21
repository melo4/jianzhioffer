# -*- coding: utf-8 -*-
# @Time    : 2019/8/21 下午2:31
# @Author  : Meng Xiao
class Solution:
    def decodeString(self, s):
        s = list(s)
        nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        stack = []
        while s:
            char = s.pop(0)
            if char != ']':
                stack.append(char)
            else:
                op1, op2 = '', ''
                popchar = stack.pop()
                while popchar != '[':
                    op2 = popchar + op2
                    popchar = stack.pop()
                while stack and stack[-1] in nums:
                    popchar = stack.pop()
                    op1 = popchar + op1
                res = int(op1) * op2
                for char in res:
                    stack.append(char)
        return ''.join(stack)
