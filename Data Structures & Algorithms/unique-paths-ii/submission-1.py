class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])

        if obstacleGrid[rows-1][cols-1] == 1 or obstacleGrid[0][0] == 1:
            return 0

        grid = [[0 for _ in range(cols)] for _ in range(rows)]

        for i in range(rows):
            if obstacleGrid[i][0] == 1:
                break
            else:
                grid[i][0] = 1 
        
        for j in range(cols):
            if obstacleGrid[0][j] == 1:
                break
            else:
                grid[0][j] = 1

        for i in range(1, rows):
            for j in range(1, cols):
                if obstacleGrid[i][j] == 1:
                    grid[i][j] = 0
                else:
                    grid[i][j] = grid[i-1][j] + grid[i][j-1]
        return grid[rows-1][cols-1]