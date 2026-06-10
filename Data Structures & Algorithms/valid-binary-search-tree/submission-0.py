# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        # q = deque([(root, float('-inf'), float('inf'))])
        # while q:
        #     node, lv, rv = q.popleft()
        #     v = node.val
        #     if not (lv < node.val < rv):
        #         return False
        #     q += [(node.left, lv, node.val)] if node.left else []
        #     q += [(node.right, node.val, rv)] if node.right else []
        # return True

        q = deque([(root)])
        while q:
            node = q.popleft()
            left, right = node.left, node.right
            lv = left.val if left else float('-inf')
            rv = right.val if right else float('inf')
            if not (lv < node.val < rv):
                return False
            if left:
                q.append((left))
            if right:
                q.append((right))
        return True