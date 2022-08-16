# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == p or root == q:
            return root
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        return root

        # my second solution, it is not work with ""binary search tree
        #
        # if not root:
        #     return None
        # if root == p or root == q:
        #     return root
        # lca_left = self.lowestCommonAncestor(root.left, p, q)
        # lca_right = self.lowestCommonAncestor(root.right, p, q)
        # if lca_left and lca_right:
        #     return root
        # return lca_left or lca_right
