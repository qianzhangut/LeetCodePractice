class Solution:
    def minTimeToType(self, word: str) -> int:
        t = "a"+ word
        ans = 0
        for i in range(len(t)-1):
            ans += min(abs(ord(t[i+1]) - ord(t[i])), 26-abs(ord(t[i+1]) - ord(t[i])))
            
        return ans + len(word)
            