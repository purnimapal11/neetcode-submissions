class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        count = 0
        visit = set()

        def dfs(r, c):
            if r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or grid[r][c] == "0" or (r,c) in visit:
                return 
            
            visit.add((r,c))
            for dr, dc in directions:
                dfs(r+dr, c+dc)



        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1" and (r,c) not in visit:
                    
                    dfs(r, c)
                    count += 1

        return count

      


        
        