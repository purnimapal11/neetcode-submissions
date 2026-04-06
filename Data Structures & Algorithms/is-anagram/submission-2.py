class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mydict = {}

        for word in s:
            if word in mydict:
                mydict[word] += 1
            else:
                mydict[word] = 1 
        
        for word in t:
            if word in mydict:
                mydict[word] -= 1
            else:
                return False
        
        for x in mydict:
            if mydict[x] > 0:
                return False
            elif mydict[x] < 0:
                return False
        
        return True