class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        m = len(s)
        t = s[::-1]

        grid = [[0 for _ in range(m+1)] for _ in range(m+1)]
        
        for i in range(1, m+1):
            for j in range(1, m+1):
                if s[i-1] == t[j-1]:
                    grid[i][j] = grid[i-1][j-1] + 1
                else:
                    grid[i][j] = max(grid[i-1][j], grid[i][j-1])


        return grid[m][m]