# -*- coding: utf-8 -*-
# @Time    : 2019/8/26 10:30
# @Author  : Meng Xiao

class Solution:
    def surfaceArea(self, grid):
        s = sum(sum([4*i+2 for i in m if i != 0]) for m in grid)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if j != len(grid[0]) - 1:
                    s -= min(grid[i][j], grid[i][j+1]) * 2
                if i != len(grid) - 1:
                    s -= min(grid[i][j], grid[i+1][j]) * 2
        return s

s = Solution()
grid = [[1,2],[3,4]]
print(s.surfaceArea(grid))

