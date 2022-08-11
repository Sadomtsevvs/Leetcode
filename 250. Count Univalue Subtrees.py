# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:

        res = [0]

        def dfs(node):
            if not node:
                return 0
            if node.left and node.right:
                dfs_left = dfs(node.left)
                dfs_right = dfs(node.right)
                if node.val == dfs_left == dfs_right:
                    res[0] += 1
                    return node.val
                return None
            if node.left:
                dfs_left = dfs(node.left)
                if node.val == dfs_left:
                    res[0] += 1
                    return node.val
                return None
            if node.right:
                dfs_right = dfs(node.right)
                if node.val == dfs_right:
                    res[0] += 1
                    return node.val
                return None
            res[0] += 1
            return node.val

        dfs(root)

        return res[0]