class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        cnt = collections.Counter("".join(c for c in licensePlate.lower() if c.isalpha()))
        return min([w for w in words if not cnt - collections.Counter(w)], key = len)