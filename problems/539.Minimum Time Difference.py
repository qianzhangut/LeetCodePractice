class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        t = sorted([int(i[:2])*60+int(i[-2:]) for i in timePoints])
        
        t1 = t[1:] + t[:1]
        
        return min((y-x)%1440 for x, y in zip(t,t1))