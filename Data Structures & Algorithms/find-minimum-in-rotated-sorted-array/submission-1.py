class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0 
        r = len(nums)-1
        tempans = float('inf')

        while l <= r:
            if nums[l] < nums[r]:       #current window is already sorted
                return min(nums[l], tempans)

            mid = (l+r)//2
            tempans = min(tempans, nums[mid])
            if nums[l] <= nums[mid]:
                l = mid+1
            else:
                r = mid-1
        return tempans
            
                
