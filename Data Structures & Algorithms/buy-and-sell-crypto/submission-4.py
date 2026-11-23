class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0 
        r = 1 
        ans = 0 

        while l < r and r < len(prices):
            if prices[r] > prices[l]:
                ans = max(ans, prices[r]- prices[l])
                r += 1
            else:
                l = r
                r += 1
        return ans 