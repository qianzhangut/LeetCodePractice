class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        return sum([v for i, v in enumerate(sorted(cost, reverse=True)) if (i+1)%3!=0])