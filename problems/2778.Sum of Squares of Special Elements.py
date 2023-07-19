class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        return sum([nums[i]*nums[i] for i in range(len(nums)) if len(nums)%(i+1)==0])