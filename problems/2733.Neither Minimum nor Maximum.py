class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        mi, ma = min(nums), max(nums)

        for i in nums:
            if i!=mi and i!=ma:
                return i

        return -1
        
 #o(1) solution      
class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        if len(nums)<3: return -1

        a, b = min(nums[0], nums[1]), max(nums[0], nums[1])
        c = nums[2]

        if (c<b and c>a): return c
        if (c<a): return a
        if (c>b): return b

        reuturn -1