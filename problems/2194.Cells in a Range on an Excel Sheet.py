class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        ans = []
        a1, a2, r1, r2 = s[0], s[3], int(s[1]), int(s[-1])
        for i in range(ord(a1), ord(a2)+1):
            ans += [chr(i)+str(j) for j in range(r1,r2+1)]
            
        return ans