class Solution:
    def numDecodings(self, s: str) -> int:
        def validating_one(c):
            if c == '0':
                return False
            else:
                return True
        
        def validating_two(c1, c2):
            # if c1 == '0':
            #     return False
            # elif c1 == '1' and int(c1+c2) >= 10 and int(c1+c2) <= 19:
            #     return True
            # elif c1 == '2' and int(c1+c2) >= 20 and int(c1+c2) <= 26:
            #     return True

            two_digit = int(c1+c2)

            return two_digit >= 10 and two_digit <= 26


        if s[0] == '0':
            return 0 
        if len(s) == 1:
            return 1 

        dp = [0]*(len(s)+1)
        dp[0] = 1
        dp[1] = 1


        for i in range(2, (len(s)+1)):
            if validating_one(s[i-1]):
                dp[i] += dp[i-1]
            if validating_two(s[i-2], s[i-1]):
                dp[i] += dp[i-2]
        
        return dp[len(s)]
        



        







        