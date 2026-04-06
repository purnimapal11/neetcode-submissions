class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mydict = set()

        for x in nums:
            if x in mydict:
                return True
            else:
                mydict.add(x)
        return False
            
        