# -*- coding: utf-8 -*-
# @Time    : 2019/4/18 下午7:04
# @Author  : Meng Xiao
class Solution:
    def FindNumsAppearOnce(self, array):
        if array == None:
            return []
        xor = 0
        for i in array:
            xor ^= i
        idxOf1 = self.getFirstIdx(xor)
        num1 = num2 = 0
        for j in range(len(array)):
            if self.IsBit(array[j], idxOf1):
                num1 ^= array[j]
            else:
                num2 ^= array[j]
        return num1, num2

    def getFirstIdx(self, num):
        # 寻找num中第一个1的位置（从右往左）
        idx = 0
        while num & 1 == 0 and idx <= 32:
            idx += 1
            num = num >> 1
        return idx

    def IsBit(self, num, indexBit):
        # 判断num的第indexBit位是不是1
        num = num >> indexBit
        return num & 1

s = Solution()
print(s.FindNumsAppearOnce([2,4,3,6,3,2,5,5]))