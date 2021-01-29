## binary search

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l, r = 1, len(arr)-1
        while l<r:
            m = l + (r-l)//2
            if arr[m]>arr[m+1]:
                r = m
            else:
                l = l+1
        return l