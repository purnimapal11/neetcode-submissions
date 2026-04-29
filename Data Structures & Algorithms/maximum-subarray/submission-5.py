class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        currSum = nums[0] 

        for i in range(1, len(nums)):
            maxSum = max(maxSum, currSum+nums[i], nums[i])
            currSum = max(currSum+nums[i], nums[i])
        return maxSum        

                
        