class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        d = {}
        
        for i in nums:
            d[i] = d.get(i, 0) + 1
        ans = [0,0]    
        for x in d.values():
            ans[0] += x//2
            ans[1] += x%2
            
        return ans