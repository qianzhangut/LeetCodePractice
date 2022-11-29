class Solution:
    def pivotInteger(self, n: int) -> int:
        res = [i for i in range(1,n+1)]
        for i in range(n):
            if sum(res[:i+1]) == sum(res[i:]):
                return i+1
        return -1