## binary serach

class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        import math
        def lcm(x, y):
            return abs(x)//math.gcd(x,y)*abs(y)
        
        l, r = 1, 10**18
        ab = lcm(a, b)
        bc = lcm(b, c)
        ac = lcm(a, c)
        abc = lcm(ab, c)
        
        while l<r:
            m = l + (r-l)//2
            k =  m // a + m // b + m // c - m // ab - m // ac - m // bc + m // abc
            if k>=n:
                r = m
            else:
                l = m+1
        return l
            