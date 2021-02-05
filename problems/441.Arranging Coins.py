## brutal force

class Solution:
    def arrangeCoins(self, n: int) -> int:
        if n < 2: return n
        for i in range(1,n+1):
            n -= i
            if n<0:
                return i-1
                
## binary search           
class Solution:
    def arrangeCoins(self, n: int) -> int:
        l , r = 0, n
        
        while l<=r:
            m = l + (r-l)//2
            res = m*(m+1)//2
            if res == n:
                return m
            if res > n:
                r = m - 1
            else:
                l = m + 1
                
        return r
        
 ## sum of arithmetic sequences 
 class Solution:
    def arrangeCoins(self, n: int) -> int:
        return int((2*n+0.25)**0.5-0.5)