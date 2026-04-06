class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        maxArr = [0]*(n)
        minArr = [0]*(n)

        maxArr[0] = nums[0]
        minArr[0] = nums[0]
        bestProd = nums[0]

        for j in range(1, n):
            maxArr[j] = max(maxArr[j-1]*nums[j], nums[j], minArr[j-1]*nums[j])
            minArr[j] = min (maxArr[j-1]*nums[j], nums[j], minArr[j-1]*nums[j])
            bestProd = max(bestProd, maxArr[j])
        return bestProd


        