class Solution:
    def combine (self, heights, mid):

        if len(heights) == 0:
            return 0

        l = mid
        r = mid
        maxArea = heights[mid]
        miniH = heights[mid]
        while l > 0 or r < len(heights)-1:

            if r < len(heights)-1 and ( l == 0 or heights[r+1] >= heights[l-1]):
                r = r+1
                miniH = min(miniH, heights[r])
            else:
                l = l-1
                miniH = min(miniH, heights[l])
            area = (r-l+1) * miniH
            maxArea = max(maxArea, area)
        return maxArea

    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
        if len(heights) == 1:
            return heights[0]
        
        mid = len(heights) // 2
        left = self.largestRectangleArea(heights[:mid])
        right = self.largestRectangleArea(heights[mid:])
        cross = self.combine(heights, mid)
        print("left" + str(left), "right"+str(right), "cross"+str(cross))
        return max(left, right, cross)
        