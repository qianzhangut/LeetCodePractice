class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        from datetime import date
        def d(s):
            return date(2022, *map(int, s.split('-')))
        first = d(max(arriveAlice, arriveBob))
        last = d(min(leaveAlice, leaveBob))
        return max(0, (last - first).days + 1)