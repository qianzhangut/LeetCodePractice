class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        ones = s.count('1')
        return '1'* (0 if ones==1 else ones-1) + '0'*(len(s)-ones) + '1'
        