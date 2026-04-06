class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        
        def dfs(i, j):
            if i >= len(matrix) or j >= len(matrix[0]) or i < 0 or j < 0:
                return 0       

            curr_max = 1
            for d in directions:
                ni, nj = i + d[0], j + d[1]
                if ni >= 0 and nj >= 0 and ni < len(matrix) and nj < len(matrix[0]) and matrix[ni][nj] > matrix[i][j]:
                    curr_max = max(curr_max, 1+dfs(ni, nj))
            return curr_max


        
        res = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                path_len = dfs(i, j)
                res = max(path_len, res)
        return res

        

        