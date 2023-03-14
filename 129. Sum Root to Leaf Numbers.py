# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        def dfs(node, prev):
            if not node.left and not node.right:
                return prev*10+node.val
            if not node.left:
                return dfs(node.right, prev*10+node.val)
            if not node.right:
                return dfs(node.left, prev*10+node.val)
            return dfs(node.left, prev*10+node.val) + dfs(node.right, prev*10+node.val)

        return dfs(root, 0)