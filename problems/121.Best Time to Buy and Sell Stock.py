class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_v, best = 1e6, 0        
        for i in prices:
            min_v = min(min_v, i)
            best = max(best, i-min_v)
        return best if best >0 else 0