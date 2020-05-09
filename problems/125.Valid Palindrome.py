class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s)==0: return True
        s = s.lower()
        sr = [e for e in s if e.isalnum()]

        return sr==sr[::-1]
        