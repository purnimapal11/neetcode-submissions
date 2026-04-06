class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = collections.defaultdict(list)
        
        def dfs(node, visit, par):
            if node in visit:
                return True
            
            visit.add(node)

            for nei in adj[node]:
                if nei == par:
                    continue
                if dfs(nei, visit, node):
                    return True
            return False


        for a, b in edges:
            visit = set()        # fresh visit for each edge check
            adj[a].append(b)
            adj[b].append(a)
            if dfs(a, visit, -1):
                return [a, b]   # this edge created the cycle


        return []
                
