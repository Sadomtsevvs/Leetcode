# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

#         if not root:
#             return 0
#         result = 0
#         stack = [root]
#         while stack:
#             result += 1
#             new_stack = []
#             for s in stack:
#                 if s.left is not None:
#                     new_stack.append(s.left)
#                 if s.right is not None:
#                     new_stack.append(s.right)
#             stack = new_stack
#         return result