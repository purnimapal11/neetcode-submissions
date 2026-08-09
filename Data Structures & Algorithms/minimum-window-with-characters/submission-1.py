class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        if t == "":
            return ""

        #frequency mapping of all characters in t
        countT = {}
        for i in t:
            if i in countT:
                countT[i] += 1
            else:
                countT[i] = 1

        l = 0
        currWin = {} #current window 
        have = 0 # how many characters currently meet the required count 
        need = len(countT) # distinct characters required
        reslen = float('inf')
        res = [-1, -1]

        for r in range(len(s)):
            currWin[s[r]] =  1 + currWin.get(s[r], 0) #add element in current window 
            if s[r] in countT and currWin[s[r]] == countT[s[r]]:
                have += 1
            while have == need:
                if ( r - l + 1) < reslen:
                    res = [l, r]
                    reslen = r-l+1
                currWin[s[l]] -= 1  #keep reducing the window from the left side 
                if s[l] in countT and currWin[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l: r+1] if reslen != float('inf') else ""

            


        
        