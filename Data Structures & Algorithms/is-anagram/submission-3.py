class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sdict = {}

        for x in s:
            if x in sdict:
                sdict[x] += 1
            else:
                sdict[x] = 1
        
        for y in t:
            if y in sdict:
                sdict[y] -= 1
            else:
                return False
        
        for key, value in sdict.items():
            if sdict[key] > 0:
                return False
        return True