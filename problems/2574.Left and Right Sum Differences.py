class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        ls, rs = 0, sum(nums[:])
        ans = []
        for i in nums:
            rs -= i
            ans.append(abs(ls-rs))
            ls += i
            
            

        return ans