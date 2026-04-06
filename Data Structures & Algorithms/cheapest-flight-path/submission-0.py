class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = collections.defaultdict(list)
        for i in range(len(flights)):
            from_i, to_i, price_i = flights[i]
            adj[from_i].append([price_i, to_i])
        
        prices = [float("inf")] * n
        prices[src] = 0
        q = deque([(0, src, 0)])
        visit = set()

        while q:
            cost, from_i, stops = q.popleft()
            if stops > k:
                continue
            
            for neicost, nei in adj[from_i]:
                nextCost = cost + neicost
                if nextCost < prices[nei]:
                    prices[nei] = nextCost
                    q.append((nextCost, nei, stops+1))

        return prices[dst] if prices[dst] != float("inf") else -1
