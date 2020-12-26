## To break an integer into sum of as many as threes will have the maximum the product of those integers

class Solution:
    def integerBreak(self, n: int) -> int:
        if n<=3:
            return n-1
        a = n//3
        b = n%3
        
        if b == 0:
            return 3**a
        elif b == 1:
            return 4*3**(a-1)
        
        return 2*3**a
        
        
## Dynamic Programing

class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0]*59
        for i in range(2, n+1):
            for j in range(1,i):
                dp[i] = max(dp[i], dp[i-j]*j)
                dp[i] = max(dp[i], (i-j)*j)
        return dp[n]