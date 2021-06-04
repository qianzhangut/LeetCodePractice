
##hashmap
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        d = {}
        
        for ind, num in enumerate(numbers):
            if target - num in d:
                return [d[target - num]+1, ind+1]
            d[num] = ind
            
        return []
        
        
## two pointer        
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
            l, r = 0, len(numbers)-1
            while l < r:
                s = numbers[l] + numbers[r]
                if s == target:
                    return [l+1, r+1]
                elif s < target:
                    l += 1
                else:
                    r -= 1