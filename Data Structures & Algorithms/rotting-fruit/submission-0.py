class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        visit = set()
        q = deque()
        fresh = 0

        def addRoom(r, c):
            if (r < 0 or c < 0 or r == len(grid) or c == len(grid[0]) or (r,c) in visit or grid[r][c] == 0):
                return 
            visit.add((r,c))
            q.append([r,c])

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append([i,j])
                    visit.add((i,j))
                if grid[i][j] == 1:
                    fresh += 1

        min = 0
        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                size_before = len(visit)
                addRoom(r+1, c)
                addRoom(r-1, c)
                addRoom(r, c+1)
                addRoom(r, c-1)
                fresh -= (len(visit) - size_before)
            min += 1

        return min if fresh == 0 else -1