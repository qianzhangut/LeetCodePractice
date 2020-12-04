## brutal force o(n^2)

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for item in range(len(nums)):
            if item not in nums:
                return item
        return len(nums)
		
		
## use formula 1 + 2 + 3 + ... + n = n*(n + 1)/2

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total = len(nums)*(len(nums)+1)//2
        for item in nums:
            total -= item
        return total            