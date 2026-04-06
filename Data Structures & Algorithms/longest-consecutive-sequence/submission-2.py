class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        myset  = set(nums)

        longest_seq = 0
        for val in nums:
            if (val-1) not in myset:
                length = 0 
                while ( val + length) in myset:
                    length += 1 
                longest_seq = max(length, longest_seq)
        return longest_seq





        