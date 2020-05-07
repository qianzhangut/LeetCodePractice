class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums=sorted(nums)
        l, r, n= 0 , nums[-1]-nums[0], len(nums)
        while l<=r:
            count, j =0, 0
            m=l+(r-l)//2
            for i in range(len(nums)):
                while j<n and nums[j]-nums[i]<=m:
                    j+=1
                count+=j-i-1
            if count>=k:
                r=m-1
            else:
                l=m+1
        return l
        