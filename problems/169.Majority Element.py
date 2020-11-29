class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = {}
        for i in nums:
            if i not in cnt:
                cnt[i] = 1
            else:
                cnt[i] += 1
            if cnt[i]> len(nums)/2:
                return i
        