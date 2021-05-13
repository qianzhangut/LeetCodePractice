class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n, pos = len(s), -float('inf')
        ans = [n] * n
        for i in [*range(n) ,*range(n)[::-1]]:
            if s[i] == c:
                pos = i
            ans[i] = min(ans[i], abs(i-pos))
        return ans
        
        
        
# DP
class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        n = len(s)
        
        ans = [0 if i == c else n for i in s]
        
        for i in range(1, n):
            ans[i] = min(ans[i], ans[i-1] + 1)
        for i in range(n-2, -1, -1):
            ans[i] = min(ans[i], ans[i+1] + 1)
            
        return ans