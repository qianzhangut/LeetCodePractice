#recursive
class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        
        
        def find(a, n):
            if n ==1:
                return a[0]
            
            for i in range(len(a)-1):
                a[i] = (a[i] + a[i+1])%10
            return find(a, n-1)
                
        return find(nums, len(nums))
        
        
#5-4-3-2-1
class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        for n in range(len(nums) - 1,0,-1):
            for i in range(n):
                nums[i] = (nums[i] + nums[i + 1]) %10
        return nums[0]