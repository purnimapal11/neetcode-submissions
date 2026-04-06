class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        

        minHeap = nums[:k]
        heapq.heapify(minHeap)

        for n in nums[k:]:
            if n > minHeap[0]:
                heapq.heappop(minHeap)
                heapq.heappush(minHeap, n)

        return minHeap[0]
            
        