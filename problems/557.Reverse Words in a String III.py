class Solution:
    def reverseWords(self, s: str) -> str:
        res = [item[::-1] for item in s.split()]
        return " ".join(res)