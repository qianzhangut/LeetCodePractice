class Solution:
    def minimumSum(self, nums: List[int]) -> int:
        if len(nums) < 3: 
            
            return -1
        min_sum = 1000
        for i in range(1,len(nums)-1):
            lm, rm = min(nums[:i]), min(nums[i+1:])
            if lm<nums[i] and nums[i]>rm:
                min_sum = min(min_sum, lm+rm+nums[i])

        return -1 if min_sum == 1000 else min_sum
        