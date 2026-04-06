class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = collections.defaultdict(list)

        for i in range(len(edges)):
            s, t = edges[i]
            adj[s].append(t)
            adj[t].append(s)

        def dfs(node):
            if node in visit:
                return 
            visit.add(node)

            for u in adj[node]:
                if u not in visit:
                    dfs(u)


        count = 0
        visit = set()
        for i in range(n):
            if i not in visit:
                count += 1 
                dfs(i)

        return count
            