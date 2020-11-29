class Solution:
    def convertToTitle(self, n: int) -> str:
        d = {i+1:chr(ord('A')+i) for i in range(26)}   
        s =''
        while n>0:
            a=(n-1)%26
            n = (n-1)//26
            s+=d[a+1]
        return s[::-1]