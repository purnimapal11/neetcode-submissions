class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        low = prices[0]
        for i in range(1, len(prices)):
            low = min(low, prices[i])
            profit = prices[i] - low
            ans = max(ans, profit)
        return ans 
        


        
        