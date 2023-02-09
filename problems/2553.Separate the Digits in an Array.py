class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans = []
        for i in nums:
            ans.extend(list(str(i)))

        return [int(j) for j in ans]