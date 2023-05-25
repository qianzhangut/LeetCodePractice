class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        ans = ''
        for i in range(len(s)):
            ans +=  min(s[i],s[len(s)-i-1] )


        return ans