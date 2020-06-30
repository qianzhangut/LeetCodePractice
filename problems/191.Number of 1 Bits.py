class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0
        for i in range(32):
            cnt += (n & 1)
            n = n >> 1
        return cnt