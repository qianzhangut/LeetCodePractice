class Solution:
    def convertToBase7(self, num: int) -> str:
        res = ''
        n = abs(num)
        while n>0:
            res += str(n%7)
            n = n//7
        if num>0:
            return res[::-1]
        elif num<0:
            return '-'+res[::-1]
        else:
            return '0'