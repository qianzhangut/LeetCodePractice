## brutala force

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        num = sorted(nums)
        res = 0
        for i in range(0, len(num),2):
            res += num[i]
            
        return res