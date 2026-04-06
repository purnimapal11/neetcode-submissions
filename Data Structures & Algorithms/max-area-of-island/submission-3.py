class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxarea = 0
        area = 0

        def dfs(r, c):
            if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or (r, c) in visit or grid[r][c] == 0:
                return 0
            visit.add((r,c))
            count = 0
            count += dfs(r+1, c)
            count += dfs(r-1, c)
            count += dfs(r, c+1)
            count += dfs(r, c-1)

            return count + 1



        visit = set()
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i,j) not in visit:
                    
                    area = dfs(i, j)
                    maxarea = max(maxarea, area)

        return maxarea

