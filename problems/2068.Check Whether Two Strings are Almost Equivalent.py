class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        d = {}
        
        for i in word1:
            d[i] = d.get(i, 0) + 1
            
        for j in word2:
            d[j] = d.get(j,0) -1
            
        return max([abs(k) for k in d.values()])<=3