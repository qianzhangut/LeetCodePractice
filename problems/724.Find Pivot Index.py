class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if sum(nums[:i]) == sum(nums[i+1:]):
                return i
        else:
            return -1
            
# use sum
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        S = sum(nums)
        leftsum = 0
        for i in range(len(nums)):
            if leftsum == (S - leftsum - nums[i]):
                return i
            leftsum += nums[i]
        return -1