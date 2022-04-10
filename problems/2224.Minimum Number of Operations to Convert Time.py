class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        c1, c2 = current.split(":"), correct.split(":")
        
        t1 = int(c1[0])*60+int(c1[1])
        t2 = int(c2[0])*60+int(c2[1])
        t = t2-t1
        
        return t//60 + t%60//15 +  t%15//5 + t%5