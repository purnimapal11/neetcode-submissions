
def subrob(nums: List[int]) -> int:
    dp = [0] * (len(nums))
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])

    for i in range(2, len(nums)):
        dp[i] = max(dp[i-1], dp[i-2]+nums[i])

    return dp[-1]

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        
        case1 = subrob(nums[0:n-1])
        case2 = subrob(nums[1:n])

        return max(case1, case2)
        