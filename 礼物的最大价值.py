# -*- coding: utf-8 -*-
# @Time    : 2019/4/15 下午8:29
# @Author  : Meng Xiao
class Solution:
    def getMaxValue(self, values, rows, cols):
        if not values or rows <= 0 or cols <= 0:
            return 0
        max_value = [0] * cols
        for i in range(rows):
            for j in range(cols):
                left, up = 0, 0
                if i > 0:
                    up = max_value[j]
                if j > 0:
                    left = max_value[j-1]
                max_value[j] = max(left, up) + values[i * cols + j]
        maxValue = max_value[cols-1]

        return maxValue
s = Solution()
matrix = [1,10,3,8,12,2,9,6,5,7,4,11,3,7,16,5]
print(s.getMaxValue(matrix, 4,4))