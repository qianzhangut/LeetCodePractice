class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        pre = [s[:i] for i in range(1,len(s)+1)]
        
        return sum([j in pre for j in words])