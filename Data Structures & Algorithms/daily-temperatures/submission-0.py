class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []

        for i in range(len(temperatures)):
            flag = False
            for j in range(i, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    flag = True
                    res.append(j-i)
                    break
            if flag == False:
                res.append(0)

        
        return res