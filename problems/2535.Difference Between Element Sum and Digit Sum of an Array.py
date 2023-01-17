class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        es = sum(nums)
        ds = sum([sum([int(j) for j in list(str(i))]) for i in nums])

        return abs(es-ds)