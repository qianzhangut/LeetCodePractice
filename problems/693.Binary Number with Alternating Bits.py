## brutal force
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        b = bin(n)[2:]
        return all(b[i] != b[i+1] for i in range(len(b)-1))

## bit operation       
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        return (n&(n>> 1)) ==0 and  (n & (n >> 2)) == (n >> 2)

## bit operation xor
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        if not n:
            return False
        num = n ^ (n >> 1)
        
        return all(i=='1' for i in bin(num)[2:])
        
        
        
        