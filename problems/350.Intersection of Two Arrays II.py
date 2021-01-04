## brutal force
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        if len(nums1)<len(nums2):
            for i in nums1:
                if i in nums2:
                    nums2.remove(i)
                    res.append(i)
        else:
            for j in nums2:
                if j in nums1:
                    nums1.remove(j)
                    res.append(j)
        return res