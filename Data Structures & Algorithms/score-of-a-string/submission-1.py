class Solution:
    def scoreOfString(self, s: str) -> int:
        ans = 0
        for x in range(1, len(s)):
            ans += abs(ord(s[x-1]) - ord(s[x]))
        return ans

        