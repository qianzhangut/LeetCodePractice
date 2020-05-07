class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m, n =len(mat), len(mat[0])
        dp = [[0 for i in range(n+1)] for j in range(m+1)]

        for x in range(1, m+1):
          for y in range(1,n+1):
            dp[x][y] = dp[x][y-1] + dp[x-1][y]-dp[x-1][y-1] + mat[x-1][y-1]


        def area(x1,y1,x2,y2):
          return dp[x2][y2] - dp[x2][y1-1]-dp[x1-1][y2]+dp[x1-1][y1-1]

        ans = 0 
        for x in range(1, m):
          for y in range(1,n):
            l, r= 0, min(m-x,n-y)+1
            while l<r:
              mid=l+(r-l)//2
              if area(x,y,x+mid,y+mid)>threshold:
                r=mid
              else:
                l=mid+1
            ans = max(ans, l)
        return ans