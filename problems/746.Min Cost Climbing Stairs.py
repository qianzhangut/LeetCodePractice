class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * len(cost)
        dp[0], dp[1] = cost[0], cost[1]
  
        for i in range(2, len(cost)):
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])
            
            
        return min(dp[-1], dp[-2])
        
        
# O(1) space solution

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        f1, f2 = cost[0], cost[1]
        
        for i in range(2, len(cost)):
            f1, f2 = f2, cost[i] + min(f1, f2)
        
        return min(f1, f2)