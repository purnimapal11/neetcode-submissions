class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        grid = [[0 for _ in range(amount+1)] for _ in range(len(coins)+1)]


        for i in range(len(coins)+1):
            grid[i][0] = 1

        for i in range(1, len(coins)+1):
            for j in range(amount+1):
                if coins[i-1] <= j :
                    grid[i][j] = grid[i-1][j] + grid[i][j-coins[i-1]]
                else:
                    grid[i][j] = grid[i-1][j]

        return grid[len(coins)][amount]

        

        