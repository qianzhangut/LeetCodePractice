## Bottom up
class Solution:
    def fib(self, n: int) -> int:
        res = {0:0, 1:1}
        for i in range(2, n+1):
            res[i] = res[i-1] + res[i-2]
        return res[n]