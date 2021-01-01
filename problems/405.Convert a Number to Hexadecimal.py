## use % and // to get each digit
class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        if num < 0:
            num = num + 2**32
        h = [str(i) for i in range(10)] + [chr(i) for i in list(range(ord('a'), ord('g')))]
        d = {i:h[i] for i in range(16)}
        res = ''
        while num > 0:
            res += d[num%16]
            num //= 16
        return res[::-1]
            
            
            