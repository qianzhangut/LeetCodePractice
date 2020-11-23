class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        l, r = 0, num
        while l<= r:
            x = (l + r) // 2
            if x*x == num:
                return True
            elif x*x > num:
                r = x - 1 
            else:
                l = x + 1 
                
        if x*x == num:
            return True
        else:
            return False
        