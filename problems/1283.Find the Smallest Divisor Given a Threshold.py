class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:

        l, r = 1,1e6
        while l<r:
          m=l+(r-l)//2
          if sum([i//m if i%m==0 else i//m +1 for i in nums])<=threshold :
            r=m
          else:
            l=m+1
        return int(l)