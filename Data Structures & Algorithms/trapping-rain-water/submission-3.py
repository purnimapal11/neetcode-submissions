class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0 
        r = len(height)-1
        leftmax = height[0]
        rightmax = height[len(height) - 1]
        water = 0 


        while l < r:

            if leftmax < rightmax:
                water += (leftmax - height[l])
                l += 1 
                leftmax = max(leftmax, height[l])
            else:
                water += (rightmax - height[r])
                r -= 1 
                rightmax = max(rightmax, height[r])
        return water




        