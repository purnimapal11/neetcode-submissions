class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for st in strs:
            count = [0]*26
            for s in st:
                count[ord(s)-ord('a')] += 1
            key = tuple(count)
            if key not in groups:
                groups[key] = []
            groups[key].append(st)

        return list(groups.values())





        