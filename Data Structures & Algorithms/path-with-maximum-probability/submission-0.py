class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj = collections.defaultdict(list)
        for i in range(len(edges)):
            src, dest = edges[i]
            adj[src].append((dest, succProb[i]))
            adj[dest].append((src, succProb[i]))

        x  = [(-1, start_node)]
        visited = set()

        while x:
            prob, node = heapq.heappop(x)
            visited.add(node)

            if node == end_node:
                return -prob

            for nei, eprob in adj[node]:
                if nei not in visited:
                    heapq.heappush(x, (prob*eprob, nei))

        return 0.0