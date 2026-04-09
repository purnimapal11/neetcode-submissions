class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mydict = {}
        for i in range (len(nums)):
            find = target - nums[i]
            if find in mydict:
                return [mydict[find], i]
            else:
                mydict[nums[i]] = i
            


            
            
        