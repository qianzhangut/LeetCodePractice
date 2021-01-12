## use strip and split

class Solution:
    def reverseWords(self, s: str) -> str:
        ss = [i.strip() for i in s.split()]
        return ' '.join(ss[::-1])