class Solution:
    def alternateDigitSum(self, n: int) -> int:
        n = str(n)

        return sum([-int(n[i]) if i%2!=0 else int(n[i]) for i in range(len(n)) ])