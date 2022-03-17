###burtal force
class Solution:
    def countElements(self, nums: List[int]) -> int:
        
        n = sorted(nums)
        ans = len(n)-2
        for i in range(1, len(n)-1):
            if n[i] == n[0] or n[i] == n[-1]:
                ans -= 1
                
        return ans if len(n)>=2 else 0
   
 ###min/max
 class Solution:
    def countElements(self, nums: List[int]) -> int:
        mi, ma = min(nums), max(nums)
        
        return sum(1 for i in nums if mi<i<ma)
   
        