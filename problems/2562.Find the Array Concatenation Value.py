class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:

        nums_r = nums[::-1]
        res = [int(str(nums[i])+str(nums_r[i])) for i in range(len(nums))]
        n = len(res)
        return sum(res[:n//2 ]) if n%2==0 else sum(res[:n//2 ]) + nums[n//2]