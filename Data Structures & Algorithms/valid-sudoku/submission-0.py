class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowset = {}
        colset = {}
        for i in range(9):
            rowset[i] = set()
            colset[i] = set()
        squareset = {}
        for i in range(3):
            for j in range(3):
                squareset[(i, j)] = set()


        for i in range(9):
            for j in range(9):
                value = board[i][j]
                if value == ".":
                    continue
                if value in rowset[i]:
                    return False
                else:
                    rowset[i].add(value)
                if value in colset[j]:
                    return False
                else:
                    colset[j].add(value)
                boxID = (i//3, j//3)
                if value in squareset[boxID]:
                    return False
                else:
                    squareset[boxID].add(value)

        return True
                


                

        