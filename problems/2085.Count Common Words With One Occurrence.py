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