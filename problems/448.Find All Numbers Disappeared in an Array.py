## use set
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = set(range(1, len(nums)+1))
        snum = set(nums)
        return list(n-snum)