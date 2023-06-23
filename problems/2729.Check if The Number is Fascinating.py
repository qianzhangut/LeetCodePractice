class Solution:
    def isFascinating(self, n: int) -> bool:
        return sorted(list('123456789')) == sorted(list(str(n)) + list(str(2*n)) + list(str(3*n)))