class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        cnt = 0
        
        for i in nums[:-1]:
            if (i+diff) in nums and ((i+diff*2) in nums):
                cnt +=1
                
        return cnt