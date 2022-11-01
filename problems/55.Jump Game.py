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
        
 ##Forward
 class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dis = 0
        for j in range( len(nums)):
            if  j>dis:
                return False
            dis = max(dis, j+nums[j])
                    
        return True
        
 #backward      
 class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dis = len(nums)-1
        for j in range( len(nums))[::-1]:
            if  j + nums[j] >=dis:
                dis = j
        return not dis