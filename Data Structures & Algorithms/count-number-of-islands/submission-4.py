class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        def call_BFS(r, c):
            queue = deque()
            queue.append((r, c))
            grid[r][c] = "0"
            while queue:
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = dr+r, dc+c
                    if (nr < 0 or nc < 0 or  nr >= len(grid) or nc >= len(grid[0]) or grid[nr][nc] == "0"):
                        continue
                    queue.append((nr, nc))
                    grid[nr][nc] = "0"


        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    call_BFS(i, j)
                    count += 1
                    
        return count 
                