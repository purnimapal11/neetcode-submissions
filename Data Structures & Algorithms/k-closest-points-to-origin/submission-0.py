class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        arr = []

        for p in points:
            x, y = p[0], p[1]

            dist = math.sqrt((x-0)**2 + (y-0)**2)
            arr.append((dist, x, y))

        heapq.heapify(arr)

        ans = []

        while len(ans) < k:
            a, b, c = heapq.heappop(arr)
            ans.append([b, c])
            

        return ans