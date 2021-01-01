## use pointer and find
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        start = 0
        for i in range(start, len(s)):
            start = t.find(s[i] , start)
            if start == -1:
                return False
            else:
                start += 1
        return True
            
## one line python

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        t = iter(t)
        return all([c in t for c in s])
            
            