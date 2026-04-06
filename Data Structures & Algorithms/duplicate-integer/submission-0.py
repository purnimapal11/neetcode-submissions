class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mydict = {}

        for num in nums:
            if num in mydict:
                return mydict[num]
            else:
                mydict[num] = True
        return False

            
        