class Solution:
    def countDigits(self, num: int) -> int:
        cnt, n  = 0, num
        while num>0:
            cnt += (n%(num%10) == 0)
            num //= 10

        return cnt
        
        
###
class Solution:
    def countDigits(self, num: int) -> int:
           return sum(x % int(y) == 0 for y in str(x))