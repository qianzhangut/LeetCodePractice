

class Solution:
    def countAndSay(self, n: int) -> str:
        if n==1:
            return '1'
        s = self.countAndSay(n-1)+'*'
        ans, cnt = '', 1
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                cnt += 1
            else:
                ans += str(cnt)+str(s[i])
                cnt = 1
        return ans
        