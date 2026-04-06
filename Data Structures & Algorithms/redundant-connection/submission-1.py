class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        par = [i for i in range(len(edges)+1)]
        rank = [1] * (len(edges)+1)
        def find(x):
            while x != par[x]:
                x = par[x]
            return x

        def union(a, b):
            a = find(a)
            b = find(b)

            if a == b:
                return False
            
            if rank[a] > rank[b]:
                par[b] = a
            else:
                par[a] = b
                if rank[a] == rank[b]:
                    rank[b] += 1
            return True


        for a, b in edges:
            if not union(a, b):
                return [a, b]

                    
                
