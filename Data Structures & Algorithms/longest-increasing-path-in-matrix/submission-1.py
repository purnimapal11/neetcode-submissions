class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        
        def dfs(i, j):
            if i >= len(matrix) or j >= len(matrix[0] or i <0 or j <0):
                return 0
            
            curr_path = 1
            for dr, dc in directions:
                nr = dr + i
                nc = dc + j
                if nr < len(matrix) and nr >= 0 and nc < len(matrix[0]) and nc >= 0 and matrix[nr][nc] > matrix[i][j]:
                    curr_path = max(curr_path, 1+dfs(nr, nc))
            return curr_path


        res = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                path_len = dfs(i, j)
                res = max(path_len, res)

        return res

        

        