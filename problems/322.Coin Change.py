class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        f = [0] + [float('inf')]* (amount +1)
        
        
        for i in range(1,amount+1):
            for j in range(len(coins)):
                if i>=coins[j]:
                    f[i] = min(f[i], f[i-coins[j]] +1)
        if f[amount] == float('inf'):
            f[amount] = -1
                    
        return f[amount]