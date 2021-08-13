class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        
        w = "".join(words)
        
        d = {}
        for i in w:
            d[i] = d.get(i, 0) + 1
            
        n = len(words)
            
        for k, v in d.items():
            if v%n != 0:
                return False
        return True
        