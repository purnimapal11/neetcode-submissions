class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = defaultdict(int)
        ans = Finalmax = 0
        

        for num in nums:
            count[num] += 1
            if Finalmax < count[num]:
                res = num
                Finalmax = count[num]
        return res

        
        