## use left and right product

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left, right = [1]*len(nums), [1]*len(nums)
        res = []
        for i in range(1,len(nums)):
            left[i] = left[i-1]*nums[i-1]
            right[len(nums) - i - 1 ] = right[len(nums)-i] *nums[len(nums)-i]
            
        for i in range(len(nums)):
            res.append(left[i]*right[i])
        return res
        