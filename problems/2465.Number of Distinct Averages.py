class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums = sorted(nums)
        
        return len(set([x + y for x, y in zip(nums, nums[::-1])]))