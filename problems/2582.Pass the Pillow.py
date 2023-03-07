class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        r = list(range(1,n+1)) + list((range(n-1, 1,-1)))

        q = (time)%(n+n-2)

        return r[q]