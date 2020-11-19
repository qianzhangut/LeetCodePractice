class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
              
        return [ [j[i] for j in A] for i in range(len(A[0]))]
        
class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
              
        return zip(*A)