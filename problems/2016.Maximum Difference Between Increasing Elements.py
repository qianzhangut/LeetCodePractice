##brutal force

class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        ans = 0
        
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if i<j:
                    ans = max(ans, nums[j]-nums[i])
        return -1 if ans == 0 else ans
        
## best time and sell
class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        
        ans, min_pointer = 0, nums[0]
        for i in range(len(nums)):
            ans = max(ans, nums[i] - min_pointer)
            min_pointer = min(min_pointer, nums[i])
            
        return -1 if ans == 0 else ans