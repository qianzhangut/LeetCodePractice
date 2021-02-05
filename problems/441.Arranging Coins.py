## brutal force

class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n < 2: return n
        for i in range(1,n+1):
            n -= i
            if n<0:
                return i-1
                
                
