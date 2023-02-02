class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        n1 = []
        for i in nums:
            n1.append(int(str(i)[::-1]))

        return len(set(nums + n1))