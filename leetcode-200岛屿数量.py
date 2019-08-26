# -*- coding: utf-8 -*-
# @Time    : 2019/8/26 下午11:14
# @Author  : Meng Xiao
class Solution:
    # 1 DFS
    def numIslands(self, grid):
        if not grid:
            return 0
        row = len(grid)
        col = len(grid[0])
        cnt = 0

        def dfs(i, j):
            grid[i][j] = '0'
            for x, y in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                tmp_i = i + x
                tmp_j = j + y
                if 0 <= tmp_i < row and 0 <= tmp_j < col and grid[tmp_i][tmp_j] == '1':
                    dfs(tmp_i, tmp_j)

        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    dfs(i, j)
                    cnt += 1
        return cnt

    # bfs
    def numIsLands_bfs(self, grid):
        if not grid:
            return 0
        row = len(grid)
        col = len(grid[0])
        cnt = 0

        def bfs(i, j):
            queue = []
            queue.append((i, j))
            grid[i][j] = '0'
            while queue:
                i, j = queue.pop(0)
                for x, y in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                    tmp_i = i + x
                    tmp_j = j + y
                    if 0 <= tmp_i < row and 0 <= tmp_j < col and grid[tmp_i][tmp_j] == '1':
                        grid[tmp_j][tmp_j] = '0'
                        queue.append((tmp_i ,tmp_j))

        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    bfs(i, j)
                    cnt += 1
        return cnt

    # 并查集
    def numIslands_b(self, grid):

        if not grid:
            return 0
        row = len(grid)
        col = len(grid[0])

        f = {}

        def find(x):
            f.setdefault(x, x)
            if f[x] != x:
                f[x] = find(f[x])
            return f[x]

        def union(x, y):
            f[find(x)] = find(y)

        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    for x, y in [[1, 0], [0, 1]]:
                        tmp_i = i + x
                        tmp_j = j + y
                        if 0 <= tmp_i < row and 0 <= tmp_j < col and grid[tmp_i][tmp_j] == '1':
                            union(tmp_i*col+tmp_j, i*col+j)

        res = set()
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    res.add(find(i*col+j))
        return len(res)