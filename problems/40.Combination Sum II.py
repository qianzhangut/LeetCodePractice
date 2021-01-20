## backtracking

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        def dfs(nums, target, idx, path, res):
            if target < 0:
                return
            elif target == 0:
                res.append(path)
            
            for i in range(idx, len(nums)):
                if i == idx or nums[i-1] != nums[i] and len(nums)>1:
                    dfs(nums, target - nums[i], i+1, path + [nums[i]], res)
                
        res = []

        dfs(candidates, target, 0, [], res)
        
        return res