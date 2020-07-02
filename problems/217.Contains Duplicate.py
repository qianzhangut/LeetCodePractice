#### use set length


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n = list(set(nums))
        if len(n) != len(nums): 
            return True
        return False
		
		
		
#### use set

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set()
        for i in nums:
            if i in s:
                return True
            else:
                s.add(i)
        return False
		
#### sort		
		
class Solution(object):
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in xrange(1,len(nums)):
            if nums[i] == nums[i-1]:
                return True
        return False