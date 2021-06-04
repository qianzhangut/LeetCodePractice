class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d = {}
        
        for ind, num in enumerate(numbers):
            if target - num in d:
                return [d[target - num]+1, ind+1]
            d[num] = ind
            
        return []