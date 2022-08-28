# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        if not root:
            return None
        if root.val <= p.val:
            return self.inorderSuccessor(root.right, p)
        min_left = self.inorderSuccessor(root.left, p)
        if min_left and min_left.val < root.val:
            return min_left
        return root

        # official solution, amazing
        #
        # successor = None
        # while root:
        #     if p.val >= root.val:
        #         root = root.right
        #     else:
        #         successor = root
        #         root = root.left
        # return successor
