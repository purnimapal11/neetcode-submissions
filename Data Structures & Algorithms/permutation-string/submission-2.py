class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s2) < len(s1):
            return False 
        
        mydict1 = {}
        for x in s1:
            if x in mydict1:
                mydict1[x] += 1
            else:
                mydict1[x] = 1
        
        mydict2 = {}
        l = 0
        for r in range(len(s2)):
            if s2[r] in mydict2:
                mydict2[s2[r]] += 1
            else:
                mydict2[s2[r]] = 1

            while r - l + 1 > len(s1):
                mydict2[s2[l]] -= 1
                if mydict2[s2[l]] == 0:
                    mydict2.pop(s2[l])
                l += 1
            if r-l+1 == len(s1) and mydict1 == mydict2:
                return True
        return False

