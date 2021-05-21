class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        res = ''
        while a or b:
            if not a: return res+b*'b'
            if not b: return res+a*'a'
            if a == b: return res+a*'ab'
            res +='aab' if a > b else 'bba'
            a, b = a-1-(a>b), b-1-(a<b)
        return res