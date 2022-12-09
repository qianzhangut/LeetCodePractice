class Solution:
    def averageValue(self, nums: List[int]) -> int:
        ans = [i for i in nums if (i%3==0 and i%2==0)]
        return int(sum(ans)/len(ans)) if len(ans)> 0 else 0