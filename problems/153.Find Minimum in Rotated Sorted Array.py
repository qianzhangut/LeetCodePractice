## brutal force

class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                return nums[i+1]
                break
        else:
            return nums[0]
            
           
           
## binary search
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        while left < right:

            mid = (left + right) // 2
                        
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                
                right = mid
                
        return nums[left]
                
        