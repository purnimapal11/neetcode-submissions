class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = collections.defaultdict(list)
        for i in range(len(times)):
            src, dest, time = times[i]
            adj[src].append((dest, time))


        visited = set()
        x = [(0, k)]

        tim = 0

        while x:
            t, node = heapq.heappop(x)
            if node in visited:
                continue
            visited.add(node)
            tim = t

            for nei, ti in adj[node]:
                if nei not in visited:
                    heapq.heappush(x, (ti + t, nei))

        if len(visited) == n:
            return tim
        else:
            return -1
            