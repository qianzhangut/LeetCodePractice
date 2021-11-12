##brutal force

class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        ans = 0
        
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if i<j:
                    ans = max(ans, nums[j]-nums[i])
        return -1 if ans == 0 else ans