## use sort method

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        
        new = sorted(nums)
        
        if len(nums)<2:
            return 0
        if new[-1] >= 2*new[-2]:
            return nums.index(new[-1])
        else:
            return -1
                