class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        n = sorted(nums)
        
        i=0
        while i<len(n):
            if n[i] == original:
                original *= 2
                i += 1
            else:
                i += 1
     
        return original