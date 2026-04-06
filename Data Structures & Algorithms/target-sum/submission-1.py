class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        def dfs(total, i):
            countpositive = 0
            countnegative = 0
            if total == target and i == len(nums):
                return 1
            if i >= len(nums):
                return 0
            
            countpositive += dfs(total + nums[i], i+1)
            countnegative += dfs(total - nums[i], i+1)
            return countpositive+countnegative
        
        return dfs(0, 0)