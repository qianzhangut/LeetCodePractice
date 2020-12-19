## count
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for i in t:
            if(t.count(i)!=s.count(i)):
                return i
        return ""
        
        
## use xor

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        code = 0
        for ch in s + t:
            code ^= ord(ch)
        return chr(code)
        
    