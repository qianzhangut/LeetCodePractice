#brutal force

class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        dw1, dw2, cnt  = {}, {}, 0
        
        for i in words1:
            dw1[i] = dw1.get(i, 0) + 1
        for j in words2:
            dw2[j] = dw2.get(j, 0) + 1
        
        for k in dw1:
            if (k in dw2) and dw1[k]==1 and dw2[k]==1:
                cnt += 1
            
        return cnt
 
#collector 
class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        from collections import Counter
        counts1 = Counter(words1)
        counts2 = Counter(words2)
        return sum( counts1[key] == counts2[key] == 1 for key in counts1 )