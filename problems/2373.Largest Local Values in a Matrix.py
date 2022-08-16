class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        ans = [[0]*(n-2) for _ in range(n-2)]
        
        for x in range(n-2):
            for y in range(n-2):
                ans[x][y] = max([grid[i][j] for i in range(x,x+3) for j in range(y,y+3)])
                
        return ans