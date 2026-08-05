class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minlen = float('inf')
        currsum = 0
        l = 0
        for r in range(len(nums)):
            currsum += nums[r]
            
            while currsum >= target:
                minlen = min(minlen, r-l+1)
                currsum -= nums[l]
                l += 1
        if minlen == float('inf'):
            return 0
        else:
            return minlen
        