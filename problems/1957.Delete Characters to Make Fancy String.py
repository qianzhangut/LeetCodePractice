class Solution:
    def makeFancyString(self, s: str) -> str:
        res, cnt = "", 0
        
        for i in range(len(s)):
            if i>0 and s[i] == s[i-1]:
                cnt += 1               
            else:
                cnt =1
            if cnt < 3:
                res += s[i]
        return res
    
    
            