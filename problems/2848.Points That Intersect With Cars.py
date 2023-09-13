class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        ans = set()
        for s, e in nums:
            for  i in range(s, e+1):
                ans.add(i)

        return len(ans)

        