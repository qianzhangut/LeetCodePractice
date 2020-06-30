class Solution:
    def reverseBits(self, n: int) -> int:

        result = 0
        for i in range(32):
            if n&(1<<i):
                result += pow(2, 32-i-1) 
        return result