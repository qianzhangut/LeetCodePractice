class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        a = set(s)
        
        for c in a:
            index = s.index(c)
            dis = distance[ord(c)-97]
            if index + dis +1 > len(s)-1 or s[index+dis+1] != c:
                return False
        return True
             