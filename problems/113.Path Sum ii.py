# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ret = []
        self.dfs(root, targetSum, [], ret)
        return ret
        
    def dfs(self, root, targetSum, path, ret):
        if root:
            if not root.left and not root.right and targetSum == root.val:
                path.append(root.val)
                ret.append(path)

            self.dfs(root.left, targetSum-root.val, path+[root.val], ret)

            self.dfs(root.right, targetSum-root.val, path+[root.val], ret)
    
        
        
        
