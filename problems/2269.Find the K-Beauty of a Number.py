class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        ans = 0
        n = str(num)
        for i in range(len(n)-k+1):
            if int(n[i:i+k]) != 0 and num % int(n[i:i+k]) == 0:
                    ans += 1
                    
        return ans