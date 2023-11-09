class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        nums = enumerate(zip_longest(*map(
                   lambda x: bin(x)[-1:1:-1],nums),fillvalue = '0'))

        return sum((1<<i)for i,arr in nums if arr.count('1') >= k)