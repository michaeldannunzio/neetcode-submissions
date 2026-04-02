# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> list[int]:
        def dfs(n, d):
            if not n:
                return None
            if d == len(res):
                res.append(n.val)
            dfs(n.right, d+1)
            dfs(n.left, d+1)

        res = []
        dfs(root, 0)
        return res
