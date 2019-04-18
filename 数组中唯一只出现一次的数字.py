# -*- coding: utf-8 -*-
# @Time    : 2019/4/18 下午7:33
# @Author  : Meng Xiao
class Solution:
    def findNumAppOnce(self, array):
        if not array or len(array) == 0:
            return
        max_length = max([len(bin(x))for x in array]) - 2
        bits_count = [0] * max_length
        for x in array:
            bit_mask = 1
            for bit_index in range(max_length-1, -1, -1):
                if x & bit_mask != 0:
                    bits_count[bit_index] += 1
                bit_mask = bit_mask << 1

        result = 0
        for count in bits_count:
            result = result << 1
            result += count % 3
        return result
s = Solution()
print(s.findNumAppOnce([2, 18, 3, 7, 3, 3, 2, 7, 2, 7]))
