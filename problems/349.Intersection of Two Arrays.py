## brutal force

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        for item in nums1:
            if item in nums2:
                result.append(item)
        return list(set(result))