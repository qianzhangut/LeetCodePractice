class Solution:
    def getLucky(self, s: str, k: int) -> int:
        stn = "".join([str(ord(i) - ord('a') + 1) for i in s])
        r1, r2 = stn, 0
        while k>0:
            r2 = sum([int(i) for i in r1])
            r1 = str(r2)
            k-=1
        return r2