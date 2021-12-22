class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        res, max_k = [], sorted(nums, reverse=True)[:k]
        for num in nums:
            if num in max_k:
                res.append(num)
                max_k.remove(num)
                if len(max_k) == 0:
                    return res