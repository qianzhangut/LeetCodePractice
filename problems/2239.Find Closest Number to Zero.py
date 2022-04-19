class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        res = nums[0]
        for a in nums: 
            if abs(res)>abs(a):
                res = a
            elif abs(res) == abs(a):
                res = max(res, a)
        return res
            