class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = 0
        sell = 1

        while sell < len(prices):
            if prices[sell] > prices[buy]:
                profit = max(profit, prices[sell] - prices[buy])
            elif prices[sell] < prices[buy]:
                buy = sell 
            sell  = sell + 1


        

        return profit


        
        