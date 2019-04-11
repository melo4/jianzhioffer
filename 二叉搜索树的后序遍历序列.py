# -*- coding: utf-8 -*-
# @Time    : 2019/4/11 下午2:57
# @Author  : Meng Xiao

class Solution:
    def VerifySquenceOfBST(self, sequence):
        if sequence == []:
            return False
        root = sequence[-1]
        for i in range(len(sequence)):
            if sequence[i] > root:
                break
        for j in range(i, len(sequence)):
            if sequence[j] < root:
                return False
        left = True
        if i > 0:
            left = self.VerifySquenceOfBST(sequence[:i])
        right = True
        if i < len(sequence) - 1:
            right = self.VerifySquenceOfBST(sequence[i:len(sequence)-1])
        return left and right

