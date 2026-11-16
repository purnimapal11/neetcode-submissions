class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        if n == 1 and k == 1:
            return 1
        
        arr = [1]*(n)
        for i in range(1, n):
            arr[i] = i+1
        
        rem = 0
        while(len(arr) > 1):
            rem = (rem + k-1)%len(arr) 
            arr.pop(rem)
        return arr[0]



