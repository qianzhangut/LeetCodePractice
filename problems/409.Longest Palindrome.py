class Solution:
    def longestPalindrome(self, s: str) -> int:
        ans = 0
        for v in collections.Counter(s).values():
            ans += v // 2 * 2
            if ans % 2 == 0 and v % 2 == 1:
                ans += 1
        return ans
        
        
        
        
        
########hash for odd numbers
class Solution:
    def longestPalindrome(self, s: str) -> int:
        hash = set()
        
        for c in s:
            if c not in hash:
                hash.add(c)
            else:
                hash.remove(c)

        return len(s)-len(hash)+1 if len(hash)>0 else len(s) 
