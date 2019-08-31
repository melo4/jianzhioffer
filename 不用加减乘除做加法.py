 # -*- coding: utf-8 -*-
# @Time    : 2019/4/18 下午10:00
# @Author  : Meng Xiao
class Solution:
    def Add(self, num1, num2):
        while num2 != 0:
            temp = num1 ^ num2
            num2 = (num1 & num2) << 1
            num1 = temp & 0xffffffff
        return num1 if num1 >> 31 == 0 else num1 - 4294967296
s = Solution()
print(s.Add(5,3))