class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        for i in range(n):
            j = i+1
            while j < n and nums[j] == nums[i] + (j-i) % 2:
                j += 1
            res = max(res, j-i)
        return res if res>1 else -1