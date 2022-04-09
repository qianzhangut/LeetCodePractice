class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        cnt = 0
        while start >0 or goal >0:
            t1, t2  = start%2, goal%2
            start = start//2
            goal = goal//2
            cnt += t1!=t2
        return cnt