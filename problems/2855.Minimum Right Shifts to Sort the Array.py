class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:

        st = sorted(nums)
        if st == nums: return 0

        for i in range(1,len(nums)+1):
            if nums[-i:] + nums[:-i] ==st:
                return i
        return -1
        