class Solution:
    def repeatedCharacter(self, s: str) -> str:
        d = {}
        
        for i in s:
            d[i] = d.get(i,0) + 1
            if d[i] == 2:
                return i