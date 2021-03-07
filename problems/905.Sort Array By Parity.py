class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
    
        return [i for i in A if i%2 ==0] + [j for j in A if j%2 ==1]
                