class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        leftarray = [0]*n
        leftarray[0] = height[0]
        maxsofar = height[0]
        for i in range(1, len(height)):
            maxsofar = max(height[i], maxsofar)
            leftarray[i] = maxsofar

        print(leftarray)

        rightarray = [0]*n
        rightarray[len(height) -1] = height[len(height)-1]
        maxsofar = height[len(height)-1]
        for i in range(len(height)-2, -1, -1):
            maxsofar = max(maxsofar, height[i])
            rightarray[i] = maxsofar
        print(rightarray)

        waterSum = 0
        for i in range(len(height)):
            waterSum += (min(leftarray[i], rightarray[i]) - height[i])
        return waterSum

            

