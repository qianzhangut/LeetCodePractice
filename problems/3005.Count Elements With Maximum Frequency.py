class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        d = {}
        for i in nums:
            d[i] = d.get(i, 0) +1
        m = 0
        for k, v in d.items():
            m = max(m, v)

        ans = 0
        for k, v in d.items():
            if v == m:
                ans += v

        return ans