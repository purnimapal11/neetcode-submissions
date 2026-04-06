class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for ele in strs:
            encoded += str(len(ele)) + "#" +ele
        return encoded

    def decode(self, s: str) -> List[str]:
        decodelist = []
        i = 0
        while i < len(s):
            j = i 
            while s[j] != "#":
                j += 1 
            length = int(s[i:j])
            decodelist.append(s[j+1: j + 1 + length])
            i = j + 1 + length 
        return decodelist