# -*- coding: utf-8 -*-
# @Time    : 2019/8/21 下午11:59
# @Author  : Meng Xiao

#左边依赖右边
class Solution:
    def canFinish(self, numCourses, prerequisites):
        indegrees = [0 for _ in range(numCourses)] # 入度
        adjacency = [[] for _ in range(numCourses)] # 邻接表
        queue = []
        for cur, pre in prerequisites:
            indegrees[cur] += 1
            adjacency[pre].append(cur)
        # 取出入度为0的课程
        for i in range(len(indegrees)):
            if not indegrees[i]:
                queue.append(i)
        # BFS
        while queue:
            pre = queue.pop(0)
            numCourses -= 1
            for cur in adjacency[pre]:
                indegrees[cur] -= 1
                if not indegrees[cur]:
                    queue.append(cur)
        return not numCourses


    # dfs做法
    def canFinish1(self, numCourses, prerequisites):
        def dfs(i, adjacency, flags):
            if flags[i] == -1:
                return True
            if flags[i] == 1:
                return False
            flags[i] = 1
            for j in adjacency[i]:
                if not dfs(j, adjacency, flags):
                    return False
            flags[i] = -1
            return True

        flags = [0 for _ in range(numCourses)]
        adjacency = [[] for _ in range(numCourses)]
        for cur, pre in prerequisites:
            adjacency[pre].append(cur)
        for i in range(numCourses):
            if not dfs(i, adjacency, flags):
                return False
        return True

