#brutal force
class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        temp = sorted(nums)
        
        return [i for i, num in enumerate(temp) if num ==target]
        
        
        
 
 ## 2 pointers
 
 class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        lt, eq = 0, 0
        
        for i in nums:
            if i < target:
                lt += 1
            elif i == target:
                eq += 1
                
        return list(range(lt, lt+eq))