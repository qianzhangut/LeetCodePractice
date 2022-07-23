class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
    
            
        ds, ts = map(Counter, (s, target))
    
            
        return min([ds[c]//ts[c] for c in ts])