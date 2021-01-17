
## use sort
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = sorted(nums)
        now, big = 1, 1
        for i in range(1,len(n)):
            if n[i] != n[i-1]:
                if n[i] == n[i-1] +1:
                    now +=1
                else:
                    big = max(big, now)
                    now = 1
        return max(now, big)        