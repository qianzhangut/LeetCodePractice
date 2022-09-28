##BFS


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        que = collections.deque([(root, False)])
        ans = 0
        while que:
            node, isLeft = que.popleft()
            if not node.left and not node.right and isLeft:
                ans += node.val 
            if node.left:  
                que.append((node.left,True))
            if node.right:
                que.append((node.right, False))
                    
        return ans

###DFS       
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def dfs(root, isLeft):
            if not root: return 0
            if not root.left and not root.right:
                return root.val if isLeft else 0
            
            return dfs(root.left, True) + dfs(root.right, False)
        
        return dfs(root, False)