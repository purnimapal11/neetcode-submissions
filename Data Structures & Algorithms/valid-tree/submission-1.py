class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n-1 :
            return False
        
        adj = collections.defaultdict(list)

        for i in range (len(edges)):
            a, b = edges[i]
            adj[a].append(b)
            adj[b].append(a)

        visit = set()

        def dfs(v, parent):

            if v in visit:
                return False

            visit.add(v)

            for u in adj[v]:
                if u == parent:
                    continue
                if dfs(u, v) == False:
                    return False
            return True

        if not dfs(0, -1):
            return False

        return len(visit) == n
