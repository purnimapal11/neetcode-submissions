class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = collections.defaultdict(list)
        indegree = [0]*numCourses
        for i in range(len(prerequisites)):
            dest, src = prerequisites[i]
            indegree[dest] += 1
            adj[src].append(dest)

        ans = []
        def dfs(node):
            ans.append(node)
            indegree[node] -= 1
            for u in adj[node]:
                indegree[u] -= 1
                if indegree[u] == 0:
                    dfs(u)

        for i in range(numCourses):
            if indegree[i] == 0:
                dfs(i)
        
        if len(ans) == numCourses:
            return ans
        else:
            return []
