class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        cnt = Counter([tuple(x) for x in grid])
        ans = 0
        for row in zip(*grid):
            ans += cnt[row]
            
        return ans
