# -*- coding: utf-8 -*-
# @Time    : 2019/3/26 下午9:03
# @Author  : Meng Xiao
class Solution:
    def hasPath(self, matrix, rows, cols, string):
        if rows < 1 or cols < 1 or matrix == None or string == None:
            return False
        visited = [0] * (rows * cols)
        pathLength = 0
        for row in range(rows):
            for col in range(cols):
                if self.hasPathCore(matrix, rows, cols, row, col, string, pathLength, visited):
                    return True
        return False

    def hasPathCore(self, matrix, rows, cols, row, col, string, pathLength, visited):
        if len(string) == pathLength:
            return True
        hasPath = False
        if row >= 0 and row < rows and col >= 0 and col < cols and matrix[row * cols + col] == string[pathLength] and not visited[row * cols + col]:
            pathLength += 1
            visited[row * cols + col] = True
            hasPath = self.hasPathCore(matrix, rows, cols, row, col - 1, string, pathLength, visited) or \
                      self.hasPathCore(matrix, rows, cols, row - 1, col, string, pathLength, visited) or \
                      self.hasPathCore(matrix, rows, cols, row, col + 1, string, pathLength, visited) or \
                      self.hasPathCore(matrix, rows, cols, row + 1, col, string, pathLength, visited)

            if not hasPath:
                pathLength -= 1
                visited[row * cols + col] = False
            return hasPath



