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
        


## use dictionary
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        dic = {}
        for ch in s:
            dic[ch] = dic.get(ch, 0) + 1
        for ch in t:
            if dic.get(ch, 0) == 0:
                return ch
            else:
                dic[ch] -= 1
                
## use ord diff
