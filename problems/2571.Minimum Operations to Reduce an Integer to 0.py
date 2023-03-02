class Solution:
    def minOperations(self, n: int) -> int:
        powers = set([1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072])
        ops = 0
        while n:
            diff, close = float('inf'), 0
            for p in powers:
                if abs(n-p) < diff:
                    diff, close = abs(n-p), p
                
            n = abs(n-close)
            ops +=1

        return ops
