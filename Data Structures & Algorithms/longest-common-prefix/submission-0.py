class Solution:

    def individual_comparison(self, s1, s2):
        i, j = 0, 0

        while i < len(s1) and j < len(s2):
            if s1[i] == s2[j]:
                i+= 1
                j+= 1
            else:
                break
        return s1[0:i]

    def longestCommonPrefix(self, strs: List[str]) -> str:
        compare = strs[0]

        for i in range(1, len(strs)):
            word_to_compare = strs[i]
            compare = self.individual_comparison(compare, word_to_compare)
        return compare