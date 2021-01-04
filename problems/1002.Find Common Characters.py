## brutal force
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        old = list(A[0])
        
        for word in A[1:]:
            new = []
            for c in word:
                if c in old:
                    new.append(c)
                    old.remove(c)
            old = new
            
        return old


## use counter

class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        import collections
        
        res = collections.Counter(A[0])
        
        for a in A:
            res &= collections.Counter(a)
            
        return list(res.elements())
        
        
        