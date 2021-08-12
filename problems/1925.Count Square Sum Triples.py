class Solution:
    def countTriples(self, n: int) -> int:
        cnt = 0
        for i in range(1, n+1):
            for j in range(i+1, n+1):
                sq = i*i + j*j
                r = int(sq**0.5)
            
                if r*r == sq and r<=n:
                    cnt += 2
        return cnt
            
              