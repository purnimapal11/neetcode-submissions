class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s) or not t:
            return ""

        Tmap = {}
        for char in t:
            Tmap[char] = Tmap.get(char, 0) + 1

        Smap = {}
        have = 0
        need = len(Tmap)

        reslen = float("inf")
        resstr = ""
        j = 0 

        for i in range(len(s)):
            
            while j < len(s) and have < need:
                char = s[j]
                if char in Tmap:
                    Smap[char] = Smap.get(char, 0) + 1
                    if Smap[char] == Tmap[char]:
                        have += 1
                j += 1


            if have == need:
                if (j - i) < reslen:
                    reslen = j - i
                    resstr = s[i:j]

            left_char = s[i]
            if left_char in Tmap:
                if Smap[left_char] == Tmap[left_char]:
                    have -= 1
                Smap[left_char] -= 1

        return resstr



                
                

