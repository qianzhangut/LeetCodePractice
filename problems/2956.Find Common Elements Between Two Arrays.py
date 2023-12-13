class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:

        return [sum(n in nums2 for n in nums1), sum(n in nums1 for n in nums2)]
        