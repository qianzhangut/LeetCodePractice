## two pointers

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums: return 0
        res, cnt, p = 1, 1, 0
        while p<len(nums)-1:
            if nums[p]< nums[p+1]:
                cnt += 1
                res = max(cnt, res)
                p+=1
            else:
                p += 1
                cnt = 1
                
        return res
                