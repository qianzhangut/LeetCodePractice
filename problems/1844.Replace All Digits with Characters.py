class Solution:
    def replaceDigits(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            if s[i].isdigit():
                res += chr(ord(s[i-1]) + int(s[i]))
            else:
                res += s[i]

        return res
            
#one line           
class Solution:
    def replaceDigits(self, s: str) -> str:
        return "".join([chr(ord(s[i-1]) + int(s[i])) if i%2 else s[i] for i in range(len(s))])
            