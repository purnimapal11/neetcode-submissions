class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = collections.defaultdict(list)
        for i in range(len(prerequisites)):
            dest, src = prerequisites[i]
            adj[src].append(dest)

        visit = set()
        recstack = set()
        res = []


        def iscyclic(visit, recstack, res, v):

            if v in recstack:
                return False

            if v in visit:
                return True

            
            recstack.add(v)
        
            for u in adj[v]:
                if iscyclic(visit, recstack, res, u) == False:
                    return False

            recstack.remove(v)
            visit.add(v)
            res.append(v)
            return True
            

        for v in range(numCourses):
            if iscyclic(visit, recstack, res, v) == False:
                return []

        return res[::-1]