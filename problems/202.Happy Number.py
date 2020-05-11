class Solution:
    def isHappy(self, n: int) -> bool:
        if n==1: return True
        d= set()
        while n!=1:
            s=0
            while(n>0):  
                s+=(n%10)**2
                n=n//10

            if s in d:
                return False
            d.add(s)
            n = s
        return True
