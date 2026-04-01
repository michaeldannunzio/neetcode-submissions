# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        stack = [root]
        diamMap = {None: (0, 0)}

        while stack:
            node = stack[-1]

            if node.left and node.left not in diamMap:
                stack.append(node.left)
            elif node.right and node.right not in diamMap:
                stack.append(node.right)
            else:
                node = stack.pop()
                lh, ld = diamMap[node.left]
                rh, rd = diamMap[node.right]
                
                height = max(lh, rh) + 1
                diam = max(lh + rh, ld, rd)
                diamMap[node] = (height, diam)

        return diamMap[root][1]
