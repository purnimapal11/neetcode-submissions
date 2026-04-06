class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dict1 = {}
        for i in s1:
            dict1[i] = 1 + dict1.get(i, 0)
        
        l = 0
        dict2 = {}
        for r in range(len(s2)):
            dict2[s2[r]] = 1 + dict2.get(s2[r], 0)

            while r - l + 1 > len(s1):
                dict2[s2[l]] -= 1
                if dict2[s2[l]] == 0:
                    dict2.pop(s2[l])
                l += 1
            if ((r-l+1) == len(s1) and dict2 == dict1):
                return True 
        return False
            