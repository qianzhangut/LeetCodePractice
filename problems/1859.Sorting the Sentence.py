class Solution:
    def sortSentence(self, s: str) -> str:
        d = {}
        for c in s.split(" "):
            d[c[-1]] = c[:-1]
            
        return " ".join([v for k, v in sorted(d.items(), key=lambda item: item[0])])