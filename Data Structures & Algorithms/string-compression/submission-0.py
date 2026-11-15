class Solution:
    def compress(self, chars: List[str]) -> int:
        l = 0 
        r = 0
        k = 0
        while r < (len(chars)):
            while r < len(chars) and chars[l] == chars[r]:
                r += 1
            chars[k] = chars[l]
            k += 1
            num = r-l
            if num > 1:
                for x in str(num):
                    chars[k] = x
                    k += 1
            l = r 
        return k
            
