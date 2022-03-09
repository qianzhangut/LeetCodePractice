class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        
        a1, a2, r1, r2 = s[0], s[3], int(s[1]), int(s[-1])
        
        return [chr(i)+str(j)  for i in range(ord(a1), ord(a2)+1) for j in range(r1,r2+1)]