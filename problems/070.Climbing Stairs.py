class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 1, 2
        if n==1: return a
        if n==2: return b
        while n>=3:
            t = a + b
            a, b = b, t
            n -=1
        return t 