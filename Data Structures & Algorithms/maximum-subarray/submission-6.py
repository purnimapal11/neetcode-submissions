class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        maxx = nums[0]

        for i in range(1, len(nums)):
            maxx = max(nums[i], maxx + nums[i])
            res = max(maxx, res)
        return res 