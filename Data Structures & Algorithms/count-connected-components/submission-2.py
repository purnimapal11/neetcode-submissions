class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = collections.defaultdict(list)
        for i in range(len(edges)):
            a, b = edges[i]
            adj[a].append(b)
            adj[b].append(a)

        visit = set()
        count = 0

        def dfs(v, visit):
            if v not in visit:
                visit.add(v)

                for u in adj[v]:
                    if u not in visit:
                        dfs(u, visit)




        for v in range(n):
            if v not in visit:
                count += 1
                dfs(v, visit)

        return count