


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adj = collections.defaultdict(list)

        for i in range(n):
            x1, y1 = points[i]
            for j in range(i+1, n):
                x2, y2 = points[j]
                dist = abs(x1-x2) + abs(y1-y2)
                adj[i].append([dist, j])
                adj[j].append([dist, i])


        visit = set()
        q = [[0,0]]
        ans = 0

        while len(visit) < n:
            wei, node = heapq.heappop(q)
            if node not in visit:
                visit.add(node)
                ans += wei
            else:
                continue
            
            for neicost, nei in adj[node]:
                if nei not in visit:
                    heapq.heappush(q, [neicost, nei])
        
        return ans