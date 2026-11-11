class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1

        visit = set()
        l = 0
        r = 0
        resLen = 0
        while r < len(s):
            while s[r] in visit:
                visit.remove(s[l])
                l+=1
            visit.add(s[r])
            resLen = max(resLen, r - l+1)
            r += 1
        return resLen

