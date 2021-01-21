## brutal force

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        for num in nums:
            res += [i + [num] for i in res]
        
        return res
        
## backtracking

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
          
        def dfs(nums, target, path, res):
            if target > 0:
                target -= 1
            elif target == 0:
                res.append(path)
            for i in range(len(nums)):
                dfs(nums[i+1:], target, path + [nums[i]], res)


        res = [[]]
        dfs(nums, 1, [], res)
        
        return res