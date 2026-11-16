class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tmap = {}

        for char in t:
            tmap[char] = tmap.get(char, 0) + 1
        
        need = len(tmap)
        have = 0 
        length = float("infinity")
        resstr = ""

        smap = {}
        i = 0 
        j = 0
        while j < len(s):
            if s[j] in tmap:
                smap[s[j]] = smap.get(s[j], 0) + 1
                if smap[s[j]] == tmap[s[j]]:
                    have += 1
            while have == need:
                if j - i + 1 < length:
                    length = j-i+1
                    resstr = s[i:j+1]
                if s[i] in smap:
                    smap[s[i]] -= 1
                    if smap[s[i]] < tmap[s[i]]:
                        have -= 1
                i += 1
                
            j += 1
        return resstr

            



                
                

