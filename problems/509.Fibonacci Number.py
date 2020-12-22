## Bottom up
class Solution:
    def fib(self, n: int) -> int:
        res = {0:0, 1:1}
        for i in range(2, n+1):
            res[i] = res[i-1] + res[i-2]
        return res[n]
        
        
## Storage reduced to O(1)
class Solution:
    def fib(self, n: int) -> int:
        if n<=1:
            return n
        if n == 2:
            return 1
        
        p1, p2, now = 1, 1 , 0
        for i in range(3, n+1):
            now = p1 + p2
            p2 = p1
            p1 = now
        return now