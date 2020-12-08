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