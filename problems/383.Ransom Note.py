## brutal force
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        m = {}
        for i in magazine:
            m[i] = m.get(i,0)
            m[i] +=1
        r = {}
        for i in ransomNote:
            r[i] = r.get(i,0)
            r[i] +=1
        return all((j in magazine) and (r[j] <= m[j]) for j in r)
        
## use