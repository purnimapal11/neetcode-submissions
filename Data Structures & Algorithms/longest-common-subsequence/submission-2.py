class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        r = len(text1)
        c = len(text2)

        grid = [[0 for _ in range(c+1)] for _ in range(r+1)]

        for i in range(1, r+1):
            for j in range(1, c+1):
                if text1[i-1] == text2[j-1]:
                    grid[i][j] = 1 + grid[i-1][j-1]
                else:
                    grid[i][j] = max(grid[i-1][j], grid[i][j-1])
        return grid[r][c]