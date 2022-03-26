class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        a = [v for i, v in enumerate(nums) if i == 0 or v != nums[i-1]]
        
        
        return sum([(a[j-1]<a[j]>a[j+1] or a[j-1]>a[j]<a[j+1]) for j in range(1,len(a)-1)])
            