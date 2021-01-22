
## backtrack
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, path, res):
            res.append(path)
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                dfs(nums[i+1:],  path + [nums[i]], res)


        res=[]
        dfs(sorted(nums), [], res)
        
        return res