## brutal force

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        for num in nums:
            res += [i + [num] for i in res]
        
        return res