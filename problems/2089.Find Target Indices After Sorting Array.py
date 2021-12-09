class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        temp = sorted(nums)
        
        return [i for i, num in enumerate(temp) if num ==target]