class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mydict = {}
        str_len = 0
        l = 0 
        for r in range(len(s)):
            if s[r] in mydict:
                mydict[s[r]] += 1
            else:
                mydict[s[r]] = 1
            while abs ( r-l+1 - max(mydict.values())) > k:
                mydict[s[l]] -= 1
                l += 1
            str_len = max(str_len, abs ( r-l+1))
        return str_len
