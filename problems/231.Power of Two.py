## didived by 2
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        while n and n%2 == 0:
            n //= 2
        return n == 1
        

## use trick n & (n-1) 
 class Solution:
    def isPowerOfFour(self, num):
        return num > 0 and num & (num-1) == 0 
        
## use bin
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        s = bin(n)[3:]
        return n !=0 and '1' not in s 