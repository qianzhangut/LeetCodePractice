class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if len(set([nums[i], nums[j], nums[k]])) == 3:
                        ans += 1
                        
        return ans
        
##combination
class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        ans = 0
        left, right = 0, len(nums)
        
        for _, freq in Counter(nums).items():
            right -= freq
            ans += left*freq*right
            left += freq
            
        return ans