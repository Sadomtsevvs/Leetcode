# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:

        ans = 0

        def dfs(node, prev, cur):
            nonlocal ans
            if not node:
                ans = max(ans, cur)
            elif prev == 'left':
                dfs(node.left, 'left', 0)
                dfs(node.right, 'right', cur + 1)
            else:
                dfs(node.left, 'left', cur + 1)
                dfs(node.right, 'right', 0)

        dfs(root.left, 'left', 0)
        dfs(root.right, 'right', 0)
        return ans
