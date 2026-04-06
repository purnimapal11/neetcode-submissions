class Solution:
    def maxArea(self, heights: List[int]) -> int:

        maximum = 0 
        L = 0 
        R = len(heights)-1
        while L < R:
            temp_max = (R - L)* min(heights[L], heights[R])
            maximum = max(maximum, temp_max)
            if heights[L] < heights[R]:
                L+= 1
            else:
                R -= 1
        return maximum
        