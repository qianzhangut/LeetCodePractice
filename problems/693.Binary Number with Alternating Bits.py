## brutal force
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        b = bin(n)[2:]
        return all(b[i] != b[i+1] for i in range(len(b)-1))
        
        