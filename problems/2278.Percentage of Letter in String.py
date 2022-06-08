class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        
        
        return 100*sum([letter==i for i in s])//len(s)