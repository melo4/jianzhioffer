# -*- coding: utf-8 -*-
# @Time    : 2019/4/9 下午4:11
# @Author  : Meng Xiao
class Solution:

    def printMatrix(self, matrix):
        if not matrix:
            return []
        rows = len(matrix)
        columns = len(matrix[0])
        start = 0
        result = []
        while columns > start*2 and rows > start*2:
            self.printMatrixInCircle(matrix, columns, rows, start, result)
            start += 1
        return result

    def printMatrixInCircle(self, matrix, columns, rows, start, result):
        endX = columns - 1 - start
        endY = rows - 1 - start
        # 左至右打印一行
        for i in range(start, endX+1):
            result.append(matrix[start][i])

        # 从上到下打印1列
        if start < endY:
            for i in range(start+1, endY+1):
                result.append(matrix[i][endX])
        # 从右往左打印一行
        if start < endX and start < endY:
            for i in range(endX-1, start-1, -1):
                result.append(matrix[endY][i])
        #从下到上打印1列 (至少需要3行两列)
        if start < endX and start + 1 < endY:
            for i in range(endY-1, start, -1):
                result.append(matrix[i][start])

