class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        return s == ''.join([i[0] for i in words])