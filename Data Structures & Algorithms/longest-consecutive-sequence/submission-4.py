class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        myset = set(nums)
        length = 0 
        long_cons = 0 

        for num in nums:
            if num - 1 not in myset:
                length = 1
                while num + length in myset:
                    length = length + 1 
                long_cons = max(length, long_cons)
        return long_cons

