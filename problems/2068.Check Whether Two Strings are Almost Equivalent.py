class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        d = {}
        
        for i in word1:
            d[i] = d.get(i, 0) + 1
            
        for j in word2:
            d[j] = d.get(j,0) -1
            
        return max([abs(k) for k in d.values()])<=3
        
## counter        
class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
    
        return all(v < 4 for v in ((Counter(word1)-Counter(word2))+(Counter(word2)-Counter(word1))).values())