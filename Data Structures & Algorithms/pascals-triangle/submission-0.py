class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        res = []
        for i in range(1, numRows+1):
            row = [1]*i
            res.append(row)
            for j in range(1, i-1):
                row[j] = res[i-2][j-1]+res[i-2][j]
        return res

        