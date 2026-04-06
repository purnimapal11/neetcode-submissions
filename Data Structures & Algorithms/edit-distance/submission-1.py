class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)

        grid = [[float('inf') for _ in range(n+1)] for _ in range(m+1)]


        for i in range(m+1):
            grid[i][0] = i
        
        for j in range(n+1):
            grid[0][j] = j

        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[j-1] == word2[i-1]:
                    grid[i][j] = grid[i-1][j-1]
                else:
                    grid[i][j] = min(grid[i-1][j], grid[i][j-1], grid[i-1][j-1])+1

        return grid[m][n]