class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        directions = [[0, -1], [0, 1], [-1, 0], [1, 0]]
        def dfs(i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == "0": 
                    return 
            grid[i][j] = "0"
            for d in directions:
                di = d[0] + i
                dj = d[1] + j


                dfs(di, dj)


        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    
                    dfs(i, j)
                    count += 1

        return count


        
        