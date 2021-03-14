class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        num = sorted(nums)[::-1]
        for i in range(len(num)-2):
            if num[i]<(num[i+1]+num[i+2]):
                return num[i]+num[i+1]+num[i+2]
        return 0