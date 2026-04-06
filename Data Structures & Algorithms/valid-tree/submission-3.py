class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = collections.defaultdict(list)

        if len(edges) > n-1:
            return False

        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        def dfs(v, visit, par):
            
            if v in visit:
                return False 
            
            visit.add(v)

            for u in adj[v]:
                if u == par:
                    continue
                if dfs(u, visit, v) == False:
                    return False
            return True
            

        visit = set()
        if dfs(0, visit, -1) == False:
                return False
        return len(visit) == n

