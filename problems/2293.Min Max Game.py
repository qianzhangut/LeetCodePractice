class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        while len(nums)>1:
            newnums = [-1]*(len(nums)//2)
            for i in range(len(newnums)):
                if i%2 == 0:
                    newnums[i] = min(nums[2 * i], nums[2 * i + 1])
                else:
                    newnums[i] = max(nums[2 * i], nums[2 * i + 1])
            nums = newnums
            
            
        return newnums[0]