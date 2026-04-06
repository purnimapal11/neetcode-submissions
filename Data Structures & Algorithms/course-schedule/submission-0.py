class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = collections.defaultdict(list)
        for i in range(len(prerequisites)):
            dest, src = prerequisites[i]
            adj[src].append(dest)


        visit = set()
        recstack = set()

        def iscyclic(visit, recstack, v):
            if v in recstack:
                return True

            if v in visit:
                return False

            visit.add(v)
            recstack.add(v)

            for u in adj[v]:
                if iscyclic(visit, recstack, u):
                    return True

            recstack.remove(v)
            return False

        for v in range(len(adj)):
            if v not in visit and iscyclic(visit, recstack, v ):
                return False
        return True
