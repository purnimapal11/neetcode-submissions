class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = collections.defaultdict(list)
        for i in range(len(times)):
            start, end, dist = times[i]
            adj[start].append([dist, end])

        
        visit = set()
        q = [(0, k)]
        res = 0

        while q:
            time, node = heapq.heappop(q)
            if node in visit:
                continue
            visit.add(node)
            res = max(res, time)
            for ti, u in adj[node]:
                if u not in visit:
                    heapq.heappush(q, (time + ti, u))

        
        if len(visit) == n:
            return res
        else:
            return -1
            