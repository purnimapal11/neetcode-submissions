class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mydict = {}

        for i in range(len(nums)):
            mydict[nums[i]] = mydict.get(nums[i], 0) + 1
        
        max_heap = []
        for key, val in mydict.items():
            heapq.heappush(max_heap, (-val, key))
        
        ans = []
        while k:
            val, key = heapq.heappop(max_heap)
            ans.append(key)
            k -= 1
        return ans 
