class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        return max(sum([1 for i in nums if i>0]), sum([1 for j in nums if j<0]))