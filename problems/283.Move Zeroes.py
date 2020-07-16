
# brutal force
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in nums:
            if i == 0:
                nums.remove(0)
                nums.append(0)
        




# double pointer

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p0, p1 = 0, 0
        
        while p0<len(nums) and p1<len(nums):
            if nums[p0] != 0:
                p0 += 1
                p1 = p0
                continue
            if nums[p1] == 0:
                p1 += 1
                continue
            nums[p0], nums[p1] = nums[p1], nums[p0]
            p0 += 1
            p1 += 1