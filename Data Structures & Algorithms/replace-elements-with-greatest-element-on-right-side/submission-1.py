class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        ans = [0]*len(arr)
        rightmax = -1
        for i in range(len(arr)-1, -1, -1):
            ans[i] = rightmax
            rightmax = max(rightmax, arr[i])
        return ans 