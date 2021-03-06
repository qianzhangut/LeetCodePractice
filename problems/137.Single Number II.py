## brutal force

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = {}
        
        for i in nums:
            d[i] = d.get(i, 0)
            d[i] += 1
            
        for i in d:
            if d[i] == 1:
                return i
                
## use count
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in nums:
            if nums.count(i) == 1:
                return i
            