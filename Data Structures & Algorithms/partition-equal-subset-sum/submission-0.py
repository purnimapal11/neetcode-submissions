class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
        if sum % 2:
            return False 

        target = sum//2
        n = len(nums)

        grid = [[False for _ in range(target+1)] for _ in range(n+1)]

        for i in range(n+1):
            grid[i][0] = True

        for i in range(1, n+1):
            for j in range(1, target+1):
                if nums[i-1] <= j:
                    grid[i][j] = grid[i-1][j] or grid[i-1][j - nums[i-1]]
                else:
                    grid[i][j] = grid[i-1][j]


        return grid[n][target]

        



        