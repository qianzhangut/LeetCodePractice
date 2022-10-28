class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dis = 0
        for j in range( len(nums)):
            dis = max(dis, j + nums[j])
            if dis >= len(nums)-1:
                return True
            if(dis<=j):
                return False;
                    
        return False