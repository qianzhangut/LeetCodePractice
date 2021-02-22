class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        p1, res = 0, ""
        
        while p1<min(len(word1) ,len(word2)):
            res += word1[p1]
            res += word2[p1]
            p1 += 1
        
        return res+word1[p1:]+word2[p1:]