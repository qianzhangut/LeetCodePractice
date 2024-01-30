class Solution:
    def countKeyChanges(self, s: str) -> int:
        cnt = 0
        for i in range(len(s)-1):
            if s[i].lower() != s[i+1].lower():
                cnt += 1
        return cnt