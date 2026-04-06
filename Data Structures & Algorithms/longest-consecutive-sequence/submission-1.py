class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return 1
        sorteddata = sorted(nums)
        myset = set(sorteddata)
        
        i = 0 
        j = 1
        max_len = 0
        while j < len(nums) and i < j:
            if sorteddata[j] - sorteddata[j-1] == 1:
                j+= 1
            elif sorteddata[j] == sorteddata[j-1]:
                i += 1 
                j += 1
            else: 
                i = j 
                j += 1 
            max_len = max(max_len, j-i)
        return max_len


        