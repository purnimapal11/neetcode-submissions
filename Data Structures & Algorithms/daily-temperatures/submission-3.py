class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stac = []
        ans = [0]*len(temperatures)

        for i in range(len(temperatures)):
            
            while stac and stac[-1][0] < temperatures[i]:
                # print("top of stack", stac[-1][0])
                # print("ans value", stac[-1][1])
                temp, idx = stac.pop()
                ans[idx]  = i - idx
            stac.append([temperatures[i], i])
        return ans

            

