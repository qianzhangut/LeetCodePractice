## brutal force

class Solution:
    def bitwiseComplement(self, N: int) -> int:
        s = bin(N)[2:]
        res = ''
        for i in s:
            if i=='0':
                res += '1'
            else:
                res += '0'
        return int(res, 2)
        

## list comprehension
class Solution:
    def bitwiseComplement(self, N: int) -> int:
        return int(''.join(['0' if i=='1' else '1' for i in bin(N)[2:]]), 2)
        
## use BitwiseOperators      
class Solution:
    def bitwiseComplement(self, N: int) -> int:
        return (1<<len(bin(N)[2:]))-1-N