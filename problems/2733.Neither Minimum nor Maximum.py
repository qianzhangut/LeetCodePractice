class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        mi, ma = min(nums), max(nums)

        for i in nums:
            if i!=mi and i!=ma:
                return i

        return -1