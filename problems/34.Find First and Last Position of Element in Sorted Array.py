## binary search

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_first(nums, target, l, r):
            l, r = 0, len(nums)
            while l < r:
                m = l + (r-l) // 2
                if nums[m] >= target:
                    r = m
                else:
                    l = m+1
            return l
        
        def find_last(nums, target, l, r):
            l, r = 0, len(nums)-1
            while l <= r:
                m = l + (r-l) // 2
                if nums[m] > target:
                    r = m  - 1
                else:
                    l = m + 1
            return r
        
        l ,r = 0, len(nums)
        left, right = find_first(nums, target, l, r),  find_last(nums, target, l, r)
        return [left,right] if left <= right else [-1, -1]