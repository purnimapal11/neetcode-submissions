class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        myset = set(nums)
        longest = 0


        for x in nums:
            if x-1 not in myset:
                length = 1 
                while x+length in myset:
                    length = length+1
                longest = max(longest, length)

        return longest

        





        