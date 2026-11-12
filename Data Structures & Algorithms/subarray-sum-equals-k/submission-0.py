class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        prefix = [0] * len(nums)
        prefix[0] = nums[0]

        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] + nums[i]
        
        mydict = {}
        mydict[0] = 1 

        count = 0 
        for i in range(len(prefix)):
            if prefix[i] - k in mydict:
                count += mydict[prefix[i] - k]
            mydict[prefix[i]] = mydict.get(prefix[i], 0) + 1
        return count 
