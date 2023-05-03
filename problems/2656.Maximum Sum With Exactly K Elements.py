class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        return max(nums)*k + int(k*(k-1)/2)