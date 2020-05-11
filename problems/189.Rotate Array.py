class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        k = k % len(nums)
        n=len(nums)
        if k != 0:            
            tmp = nums[-k:]
            for j in range(len(nums)-1, k-1, -1):
                nums[j] = nums[j-k]
            nums[:k] = tmp
