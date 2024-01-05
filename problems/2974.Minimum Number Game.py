class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nn = sorted(nums)
        return list(sum(zip(nn[1::2], nn[::2]), ()))