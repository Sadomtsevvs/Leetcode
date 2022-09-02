# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        result = 0
        stack = [(root, -10 ** 4 - 1)]
        while stack:
            node, mx = stack.pop()
            if node.val >= mx:
                mx = node.val
                result += 1
            if node.left:
                stack.append((node.left, mx))
            if node.right:
                stack.append((node.right, mx))
        return result

        # first solution, slow

#         result = 0

#         def dfs(node, biggest_from_root):
#             nonlocal result
#             if not node:
#                 return
#             if node.val >= biggest_from_root:
#                 result += 1
#             dfs(node.left, max(node.val, biggest_from_root))
#             dfs(node.right, max(node.val, biggest_from_root))

#         dfs(root, -10**4 - 1)
#         return result