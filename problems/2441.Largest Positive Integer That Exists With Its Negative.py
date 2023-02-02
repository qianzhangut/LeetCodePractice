

## O(n^2)
class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        m = max(nums)

        for i in reversed(range(m+1)):
            if (i in nums) and (-i in nums):
                return i

        return -1