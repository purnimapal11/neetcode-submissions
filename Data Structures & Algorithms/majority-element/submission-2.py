class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        mydict = {}

        for i in range(len(nums)):
            mydict[nums[i]] = mydict.get(nums[i], 0) + 1
        
        ans = max(mydict, key=mydict.get)
        return ans
