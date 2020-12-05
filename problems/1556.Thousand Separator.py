
## Get modulus and floor division
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

## use list reverse
class Solution:
    def thousandSeparator(self, n: int) -> str:
            
        s = str(n)[::-1]

        r = ""

        for i in range(0, len(s), 3):
            r += s[i:i+3] + '.'
        return r[-2::-1]
        

           