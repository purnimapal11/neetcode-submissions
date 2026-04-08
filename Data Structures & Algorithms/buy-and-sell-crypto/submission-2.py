class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_so_far = prices[0]
        ans = 0

        for i in range(1, len(prices)):
            min_so_far = min(min_so_far, prices[i])
            ans = max(ans, prices[i]- min_so_far)

        return ans 


        
        