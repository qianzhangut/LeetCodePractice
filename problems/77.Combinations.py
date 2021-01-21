## backtracking

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        candidates = [i+1 for i in list(range(n))]
        
        def dfs(nums, target, path, res):
            if target > 0:
                target -= 1
            elif target == 0:
                res.append(path)
                return
            
            for i in range(len(nums)):
                dfs(nums[i+1:], target, path + [nums[i]], res)
                
        res = []
        dfs(candidates, k, [], res)
        
        return res