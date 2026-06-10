# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        def dfs(node):
            if not node:
                return 0

            lh, rh = dfs(node.left), dfs(node.right)
            return max(lh, rh) + 1

        lh, rh = dfs(root.left), dfs(root.right)
        return abs(lh - rh) <= 1
