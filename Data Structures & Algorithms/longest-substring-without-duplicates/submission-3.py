class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visit = set()
        l = 0
        maxx = 0

        for r in range(len(s)):
            while s[r] in visit:
                visit.remove(s[l]) 
                l += 1
            visit.add(s[r])
            maxx = max(maxx, r - l +1 )


        return maxx
                    



                
                

