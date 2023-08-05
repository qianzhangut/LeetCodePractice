class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])

        rowSum, colSum = list(map(sum, grid)), list(map(sum, zip(*grid)))
        
        return [[2*(rowSum[r] + colSum[c]) - m-n
                 for c in range(n)] for r in range(m)]