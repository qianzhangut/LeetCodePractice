## sliding window
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        res = now = sum(nums[:k])
        for i in range(k,len(nums)):
            now += nums[i] - nums[i-k]
            if now>res:
                res = now
        return res/k

## cumulative sum
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = nums
        
        for i in range(1, len(nums)):
            n[i] = n[i-1] + nums[i]
        res = n[k-1]
        for i in range(k, len(n)):
            res = max(res, n[i]-n[i-k])
        return res/k