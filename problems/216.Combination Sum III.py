
## back tracking

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        candi = list(range(1, 10))
        
        def dfs(nums, target, path, res):
            if target<0:
                return
            elif target == 0 and len(path) == k:
                res.append(path)
                return
            for i in range(len(nums)):
                dfs(nums[i+1:], target- nums[i], path + [nums[i]], res)
                
            return res
        
        res=[]
        dfs(candi, n, [], res)
            
        return res