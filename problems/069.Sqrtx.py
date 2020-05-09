#binary search
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1 : return 1
        if x == 0 : return 0
        l, r = 0, x
        while l<r:
            mid = l +(r-l)//2
            if mid**2==x:
                return mid
            elif mid**2>x:
                r = mid
            else:
                l = mid+1
        return l-1 

#netwon's method

class Solution:
    def mySqrt(self, x: int) -> int:
        res = 1.0
        while abs(res * res - x) > 0.5:
            res = (res + x / res) / 2
        return int(res)