class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = {}
        ans = []

        for x in strs:
            sorted_word = "".join(sorted(x))
            if sorted_word in words:
                words[sorted_word].append(x)
            else:
                words[sorted_word] = [x]
        
        for key, value in words.items():
            ans.append(value)
        return ans 