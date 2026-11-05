class Solution:
    def longestPalindrome(self, s: str) -> str:
        reslen = 0
        resstr = ""

        if len(s) == 1:
            return s

        for x in range(len(s)):
            i = x
            j = x


            while i >= 0 and j < len(s) and s[i] == s[j]:
                if (j - i + 1 ) > reslen:
                    reslen = j-i+1
                    resstr = s[i:j+1]
                i -= 1
                j += 1

                    

            i = x-1
            j = x
            while i >= 0 and j < len(s) and s[i] == s[j]:
                if (j - i + 1) > reslen:
                    reslen = j-i+1
                    resstr = s[i:j+1]  
                i -= 1
                j += 1  
 
        return resstr  

