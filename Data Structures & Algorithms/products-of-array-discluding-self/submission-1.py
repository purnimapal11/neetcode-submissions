class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [0]*len(nums)
        suffix = [0]*len(nums)
        prefix = [0]*len(nums)

        left = 1
        for i in range(0, len(nums)):
            prefix[i] = left
            left *= nums[i]
        print(prefix)
        
        right = 1 
        suffix[len(nums)-1] = 1
        for i in range(len(nums)-1, -1, -1):
            suffix[i] = right
            right *= nums[i]
        
        print(suffix)

        for i in range(len(nums)):
            output[i] = suffix[i]*prefix[i]

        return output




        