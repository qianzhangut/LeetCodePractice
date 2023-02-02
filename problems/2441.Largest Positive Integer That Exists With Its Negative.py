

## O(n^2)
class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        m = max(nums)

        for i in reversed(range(m+1)):
            if (i in nums) and (-i in nums):
                return i

        return -1
        
        
##O(n)
class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        ans = -1001
        m = set(nums)
        for i in nums:
            if (i in m) and (-i in m):
                ans = max(ans, abs(i))

        return -1 if ans==-1001 else ans