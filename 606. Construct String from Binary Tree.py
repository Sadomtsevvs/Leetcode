# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        val = str(root.val)
        if not root.left and not root.right:
            return val
        if root.left:
            if root.right:
                return val + "(" + self.tree2str(root.left) + ")(" + self.tree2str(root.right) + ")"
            else:
                return val + "(" + self.tree2str(root.left) + ")"
        else:
            return val + "()(" + self.tree2str(root.right) + ")"
