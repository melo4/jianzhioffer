# -*- coding: utf-8 -*-
# @Time    : 2019/4/24 下午8:37
# @Author  : Meng Xiao
class Graph(object):
    def __init__(self):
        self.node_neighbors = {}
        self.visited = {}

    def add_nodes(self, nodelist):
        for node in nodelist:
            self.add_node(node)

    def add_node(self, node):
        if not node in self.nodes():
            self.node_neighbors[node] = []

    def add_edge(self, edge):
        u, v = edge
        if v not in self.node_neighbors[u] and u not in self.node_neighbors[v]:
            self.node_neighbors[u].append[v]
            if u != v:
                self.node_neighbors[v].append(u)

    def nodes(self):
        return self.node_neighbors.keys()

    # 递归DFS
    def dfs_re(self, root=None):
        order = []
        def dfs(node):
            self.visited[node] = True
            order.append(node)
            for n in self.node_neighbors[node]:
                if not n in self.visited:
                    dfs(n)
        if root:
            dfs(root)

        for node in self.nodes():
            if not node in self.visited:
                dfs(node)
        self.visited = {}
        print(order)
        return order

