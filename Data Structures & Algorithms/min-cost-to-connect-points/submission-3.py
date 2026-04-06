class DSU:
    def __init__(self, n):
        self.parent = list(range(n+1))
        self.size = [1]*(n+1)

    def find(self, node):
        # if self.parent[node] != node:
        #     self.parent[node] = self.find(self.parent[node])
        # return self.parent[node] 

        while node != self.parent[node]:
            node = self.parent[node]
        return node

    def union(self, u, v):
        self.link(self.find(u), self.find(v))

    def link(self, a, b):
        if self.size[a] > self.size[b]:
            self.parent[b] = a
        else:
            self.parent[a] = b
            if self.size[a] == self.size[b]:
                self.size[b] += 1
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        dsu = DSU(n)

        edges = []
        

        for i in range(len(points)):
            x1 , y1 = points[i]
            for j in range(i+1, len(points)):
                x2, y2 = points[j]
                dist = abs(x1-x2) + abs(y1-y2)
                edges.append((dist, i, j))

        edges.sort()

        res = 0

        for dist, u, v in edges:
            if dsu.find(u) != dsu.find(v):
                res += dist
                dsu.union(u, v)
        return res 

        
        


     