class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        rows, cols = len(board), len(board[0])
        directions = [[0,1], [0,-1], [1,0], [-1,0]]


        def capture():
            q = deque()
            for i in range(rows):
                for j in range(cols):
                    if (i == 0 or i == rows-1 or j == 0 or j == cols-1)  and (board[i][j] == "O"):
                        q.append((i,j))

            while q:
                r, c = q.popleft()
                # if board[r][c] == 'O'
                board[r][c] = 'T'
                for dr, dc in directions:
                    if 0<= dr+r < rows and 0<= dc+c< cols and board[dr+r][dc+c] == 'O':
                        q.append((dr+r, dc+c))


        capture()


        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "T":
                    board[i][j] = "O"


