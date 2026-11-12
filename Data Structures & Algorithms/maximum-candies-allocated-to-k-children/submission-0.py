class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if sum(candies) < k :
            return 0 
        
        l = 1 
        r = max(candies)
        ans = r 

        while l <= r:
            mid = (l+r) // 2
            count = 0 
            for candy in candies:
                count += (candy//mid)
            if count < k:
                r = mid - 1
            else:
                ans = mid
                l = mid + 1
        return ans 

