## use count 

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        d = {}
        for num in nums:
            d[num] = nums.count(num)
            if d[num]>1:
                return num
        