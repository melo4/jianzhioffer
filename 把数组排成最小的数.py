# -*- coding: utf-8 -*-
# @Time    : 2019/4/15 下午5:13
# @Author  : Meng Xiao
class Solution:
    def printminnumber(self, numbers):
        if not numbers:
            return ''
        str_num = [str(m) for m in numbers]
        for i in range(len(numbers)-1):
            for j in range(i+1, len(numbers)):
                if str_num[i] + str_num[j] > str_num[j] + str_num[i]:
                    str_num[i], str_num[j] = str_num[j], str_num[i]

        return ''.join(str_num)
s = Solution()
print(s.printminnumber([3,32,321]))