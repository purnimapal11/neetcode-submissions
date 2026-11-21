class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0 
        l = 0 
        r = len(nums)-1

        while l <= r:
            if nums[l] == val:
                nums[l], nums[r] = nums[r], nums[l]
                r -= 1
                continue
            l += 1
            k += 1
        return k