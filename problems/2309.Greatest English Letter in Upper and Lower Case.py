class Solution:
    def greatestLetter(self, s: str) -> str:
        
        s = set(s)
        up, lo = ord('A'), ord('a')
        for i in range(25,-1,-1):
            if chr(up + i) in s and chr(lo + i) in s:
                return chr(up+i)
        return ""