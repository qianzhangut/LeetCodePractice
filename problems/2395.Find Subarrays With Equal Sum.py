class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        sums = set()

        for i in range(len(nums)-1):

            if (nums[i] + nums[i+1]) in sums:
                return True

            else:
                sums.add(nums[i] + nums[i+1])

        return False