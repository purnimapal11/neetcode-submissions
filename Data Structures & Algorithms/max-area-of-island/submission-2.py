class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        MaxArea = 0
        area = 0
        directions = [[0, -1], [0, 1], [-1, 0], [1, 0]]
        def dfs(i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0: 
                    return 0
            
            grid[i][j] = 0
            count = 0
            for d in directions:
                di = d[0] + i
                dj = d[1] + j

                
                count += dfs(di, dj)
            return 1+ count 


        
        for i in range(len(grid)):
            for j in range(len(grid[0])):

                if grid[i][j] == 1:
                    
                    area = dfs(i, j)
                    
                
                MaxArea = max(MaxArea, area)

        return MaxArea