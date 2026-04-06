class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        stack = [] #pair of values, [temp, index]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackt, stackid = stack.pop()
                res[stackid] = (i-stackid)
            stack.append([t, i])
        return res

            