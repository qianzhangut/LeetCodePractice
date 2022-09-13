class Solution:
    def partitionString(self, s: str) -> int:
        check = set()
        ans = 1
        
        for c in s:
            if c in check:
                check = set()
                ans +=1
            check.add(c)
            
        return ans