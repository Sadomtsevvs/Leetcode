# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:

        # my second solution

        if not root:
            return ''
        left = self.tree2str(root.left)
        right = self.tree2str(root.right)
        val = str(root.val)
        if right:
            return val + '(' + left + ')' + '(' + right + ')'
        elif left:
            return val + '(' + left + ')'
        return val

        # val = str(root.val)
        # if not root.left and not root.right:
        #     return val
        # if root.left:
        #     if root.right:
        #         return val + "(" + self.tree2str(root.left) + ")(" + self.tree2str(root.right) + ")"
        #     else:
        #         return val + "(" + self.tree2str(root.left) + ")"
        # else:
        #     return val + "()(" + self.tree2str(root.right) + ")"
