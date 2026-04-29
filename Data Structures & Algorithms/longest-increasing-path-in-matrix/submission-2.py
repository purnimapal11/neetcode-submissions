class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        dp = {}
        

        def dfs(i, j, prevVal):
            if i < 0 or j < 0 or i >= len(matrix) or j >= len(matrix[0]) or matrix[i][j] <= prevVal:
                return 0
            if (i, j) in dp:
                return dp[(i, j)]

            res = 1
            for d in directions:
                newr = i + d[0]
                newc = j + d[1]
                res = max(res, 1 + dfs(newr, newc, matrix[i][j]))
            dp[(i, j)] = res
            return res

        maximum = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                dfs(i, j, -1)
   
        return max(dp.values())

        

        