class Solution:
    def titleToNumber(self, s: str) -> int:
        n, num = len(s), 0
        if n == 1: return ord(s[0]) - ord('A') + 1

        for i in range(n):
            num +=(ord(s[i]) -ord('A')+1)*(26**(n-i-1))
        return num