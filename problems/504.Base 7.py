class Solution:
    def convertToBase7(self, num: int) -> str:
        res = ''
        n = abs(num)
        while n>0:
            res += str(n%7)
            n = n//7
        if num==0:
            return '0'
        else:
            [res[::-1], '-'+res[::-1]][num<0]