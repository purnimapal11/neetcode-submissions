class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        ans = []
        nums.sort()
        for i in range(len(nums)):
            j = i+1 
            k = len(nums)-1

            if i > 0 and nums[i] == nums[i-1]:
                continue

            while j < k:
                if nums[k] + nums[j] + nums[i] == 0 :
                    ans.append([nums[i], nums[j], nums[k]])
                    j += 1 
                    k -=1 
                    while nums[j] == nums[j-1] and j < k:
                        j += 1 
                    while nums[k] == nums[k+1] and j < k:
                        k -=1 
                elif nums[j] + nums[k] + nums[i] < 0:
                    j += 1 
                else:
                    k -=1 

        return ans  
        
        