class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if sum(nums[:i]) == sum(nums[i+1:]):
                return i
            
        return -1
        
        
## pointer 
class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        s, p_sum = sum(nums), 0
        for i, num in enumerate(nums):
            if p_sum == (s - num) / 2.0:
                return i
            p_sum += num
        return -1