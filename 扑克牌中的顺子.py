# -*- coding: utf-8 -*-
# @Time    : 2019/4/18 下午9:31
# @Author  : Meng Xiao
class Solution:
    def IsContinuous(self, numbers):

        if not numbers or len(numbers) == 0:
            return False

        transdict = {'A':1,'J':11,'Q':12,'K':13}
        for i in range(len(numbers)):
            if numbers[i] in transdict.keys():
                numbers[i] = transdict[numbers[i]]
        numbers = sorted(numbers)
        num_0 = 0
        num_gap = 0

        i = 0
        while i < len(numbers) and numbers[i] == 0:
            num_0 += 1
            i += 1
        front = num_0
        behind = front + 1
        while behind < len(numbers):
            if numbers[front] == numbers[behind]:
                return False
            num_gap += numbers[behind] - numbers[front] - 1
            front = behind
            behind += 1
        return False if num_gap > num_0 else True
s = Solution()
print(s.IsContinuous([1,3,5,4,0]))