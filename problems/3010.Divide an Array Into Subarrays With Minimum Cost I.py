class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        s = sorted(nums[1:])
        return nums[0] + s[0] + s[1]