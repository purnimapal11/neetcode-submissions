class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1

        visit = set()
        l = 0
        r = 0 
        resLen = 0
        resstr = ""
        while r < len(s):
            if s[r] not in visit:
                visit.add(s[r])
                r += 1
            elif s[r] in visit:
                resLen = max(resLen, r - l)
                resstr = max(resstr, s[l:r])
                while s[r] in visit:
                    visit.remove(s[l])
                    l+=1
        resLen = max(resLen, r - l)
        resstr = max(resstr, s[l:r])
        return resLen

