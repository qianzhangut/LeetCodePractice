class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        d ={}
        for i in nums:
            d[i] = d.get(i, 0) + 1
        return all(j%2==0 for j in d.values())