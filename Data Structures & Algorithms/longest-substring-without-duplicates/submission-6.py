class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        visit = set()
        lenn = 0

        j = 0
        for i in range(len(s)):
            while s[i] in visit:
                visit.remove(s[j])
                j += 1
            visit.add(s[i])
            lenn = max(lenn, abs(i-j)+1)
        return lenn

            
                    



                
                

