## backtracking

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(candidates, target, path, res):
            if target < 0 :
                return
            elif target == 0:
                res.append(path)
                return
                
            for i in range(len(candidates)):
                dfs(candidates[i:], target- candidates[i], path + [candidates[i]], res)
                
        res = []
        dfs(candidates, target, [], res)
        return res