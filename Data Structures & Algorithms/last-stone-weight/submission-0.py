class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            x = heapq.heappop(stones)
            print(x)
            y = heapq.heappop(stones)
            print(y)

            if x < y:
                heapq.heappush(stones, x-y)
        
        stones.append(0)
        return abs(stones[0])

        