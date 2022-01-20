## brutal force
class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        t = list(zip(*matrix))
        res = matrix + t
        
        return all([len(set(i))==len(matrix[0]) for i  in res])