class Solution:
    def tribonacci(self, n: int) -> int:
        t0, t1, t2 = 1,0,0
        for i in range(n):          
            t0, t1 , t2 = t1, t2 , t0+t1+t2
            

        return t2