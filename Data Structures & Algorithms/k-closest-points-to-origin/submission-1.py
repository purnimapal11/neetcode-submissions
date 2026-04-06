class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dist = []

        for x, y in points:
            d = math.sqrt((x-0)**2 + (y-0)**2)
            dist.append([d, (x, y)])

        heapq.heapify(dist)
        ans = []
        while len(ans) < k:
            node = heapq.heappop(dist)
            x, y = node[1]
            ans.append([x,y])
        return ans 
