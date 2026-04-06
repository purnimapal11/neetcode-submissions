class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)

        grid = [[0 for _ in range(n+1)] for _ in range(m+1)]

        for i in range(n+1):
            grid[0][i] = 0 

        for j in range(m+1):
            grid[j][0] = 0

        for i in range(1, m+1):
            for j in range(1, n+1):
                if text1[j-1] == text2[i-1]:
                    grid[i][j] = grid[i-1][j-1] + 1
                else:
                    grid[i][j] = max(grid[i-1][j], grid[i][j-1])
        return grid[m][n]