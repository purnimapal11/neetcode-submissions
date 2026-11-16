class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        cache = {} #for TLE 

        def count(i, k, prev, prev_cnt):
            if (i, k, prev, prev_cnt) in cache: #(i, k, prev, prev_cnt)is the key
                return cache[(i, k, prev, prev_cnt)]

            if k < 0: #to block the recursion tree delete call where we decrement k
                return float("inf")

            if i == len(s):
                return 0
            if s[i] == prev:
                # incr is for adding that extra space from double, triple digit
                incr = 1 if prev_cnt in [1, 9, 99] else 0
                res = incr + count(i+1, k, s[i], prev_cnt+1)

            else:
                res = min(
                    count(i+1, k-1, prev, prev_cnt), 
                    1 + count(i+1, k, s[i], 1) #1 is being added because new char is part of the compressed string now
                )
            cache[(i, k, prev, prev_cnt)] = res 
            return res


        return count(0, k, "", 0)
        
