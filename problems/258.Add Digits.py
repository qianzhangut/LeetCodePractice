class Solution:
    def addDigits(self, num: int) -> int:
        res = 11
        while res >= 10:
            tmp = 0
            while num > 0:
                tmp += num %10
                num = num // 10
            res = tmp
            num = res
        return res