class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        return min(list(set(nums1)&set(nums2))) if set(nums1)&set(nums2) else min(min(nums1)*10 + min(nums2), min(nums2)*10 + min(nums1))