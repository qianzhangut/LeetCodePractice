class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        

        return max((x*x+y*y, x*y) for x, y in dimensions)[1]   