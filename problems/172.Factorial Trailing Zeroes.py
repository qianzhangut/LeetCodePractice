class Solution:
    def trailingZeroes(self, n: int) -> int:
        num, cnt = 5, 0
 
        while num <= n:
            cnt += n//num
            num *= 5
        return cnt