class Solution:
    def countPrimeSetBits(self, L: int, R: int) -> int:
        prime = {2,3,5,7,11,13,17,19,23}
        cnt = 0
        for i in range(L, R+1):
            sb = bin(i)[2:].count('1')
            if sb in prime:
                cnt += 1
        return cnt