## brutal force
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        for x in range(16):
            res = 4**x
            if res == n:
                return True
                break
        return False
        
        
 ##use bin
 class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        s = bin(n)[3:]
        return n !=0 and '1' not in s and len(s)%2 == 0
        
 ## divide by 4    
 class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        while n and n%4 == 0:
            n //= 4
        return n == 1
 
## use trick n & (n-1) 
 class Solution:
    def isPowerOfFour(self, num):
        return num > 0 and num & (num-1) == 0 and 0b1010101010101010101010101010101 & num == num 
            