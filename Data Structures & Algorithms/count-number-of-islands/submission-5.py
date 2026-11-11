class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        def DFS(r, c):
            if (r < 0 or c < 0 or  r >= len(grid) or c >= len(grid[0]) or grid[r][c] == "0"):
                        return 
            
            grid[r][c] = "0"
            

            for dr, dc in directions:
                nr, nc = dr+r, dc+c
                DFS(nr, nc)
                    
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    DFS(i, j)
                    count += 1
                    
        return count 
                