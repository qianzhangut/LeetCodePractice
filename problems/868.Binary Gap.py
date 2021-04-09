class Solution:
    def binaryGap(self, n: int) -> int:
        b = bin(n)[2:]
        
        p = [i for i in range(len(b)) if b[i]=='1']        
        return max([b - a for a, b in zip(p, p[1:])] or [0])