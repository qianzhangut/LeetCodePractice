class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        p, n = [i for i in nums if i>0],[j for j in nums if j<0]
        ans = []
        for k in range(len(p)):
            ans.append(p[k])
            ans.append(n[k])
        return ans