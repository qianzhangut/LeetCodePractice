class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        
        n = len(words)

        for left in range(n):
            if words[(startIndex+left)%n ] == target: break
        else: return -1    

        for right in range(n):
            if words[(startIndex-right)%n] == target: break
  
        return  min(left, right)
        
        
## Two relative distance

class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        
        n = len(words)
        final_posn = float("inf")
        for i in range(n):
            if words[i] == target:
                final_posn = min(final_posn, abs(i-startIndex), n-abs(i-startIndex))
        return -1 if final_posn == float("inf") else final_posn