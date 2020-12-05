class Solution:
    def thousandSeparator(self, n: int) -> str:
        if n<1000:
            return str(n)
        else: 
            t = ''
            while n>999:
                b = n%1000
                t = '.' + '%.3d'%b + t
                n = n//1000
            return str(n)+t