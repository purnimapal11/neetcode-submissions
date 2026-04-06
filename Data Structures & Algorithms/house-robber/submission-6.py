class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # if len(nums) == 1:
        #     return nums[0]
        # nums1 = nums[0]

        # nums2 = nums[1]

        # for i in range(2, len(nums)):
        #     if i%2 == 0:
        #         nums1 += nums[i]
        #     else:
        #         nums2 += nums[i]

        # return max(nums1, nums2)

        dp = [0]*len(nums)
        if len(nums) == 1:
            return nums[0]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])

        return max(dp[-1], dp[-2])
        