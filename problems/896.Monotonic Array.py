## use sort
class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        return sorted(A) == A or sorted(A) == A[::-1]
        
## O(n)
class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        dif = []
        for i in range(1, len(A)):
            dif.append(A[i]-A[i-1])
            
        return all(x>= 0 for x in dif) or all(x<= 0 for x in dif)