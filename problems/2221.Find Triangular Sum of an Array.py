class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        
        
        def find(a, n):
            if n ==1:
                return a[0]
            
            for i in range(len(a)-1):
                a[i] = (a[i] + a[i+1])%10
            return find(a, n-1)
                
        return find(nums, len(nums))