class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        if len(nums) == 1:
            return [str(nums[0])]
        
        lo, hi = 0, 1
        result = []

        while hi <= len(nums):
            if hi < len(nums) and nums[hi] == nums[hi-1] + 1:
                hi += 1
            else:
                if hi - lo == 1:
                    result.append(str(nums[lo]))
                else:
                    result.append(f"{nums[lo]}->{nums[hi-1]}")
                lo, hi = hi, hi + 1
        return result