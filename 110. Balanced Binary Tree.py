# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def height(node):
            if not node:
                return 0
            h_l = height(node.left)
            if h_l == -1:
                return -1
            h_r = height(node.right)
            if h_r == -1:
                return -1
            if abs(h_l - h_r) > 1:
                return -1
            return 1 + max(h_l, h_r)

        return height(root) != -1

        #         if not root:
        #             return True

        #         def height(node):
        #             if not node:
        #                 return 0
        #             h_l = height(node.left)
        #             h_r = height(node.right)
        #             if h_l == float('inf') or h_r == float('inf') or abs(h_l - h_r) > 1:
        #                 return float('inf')
        #             return 1 + max(h_l, h_r)

        #         h_l = height(root.left)
        #         h_r = height(root.right)

        #         if h_l == float('inf') or h_r == float('inf') or abs(h_l - h_r) > 1:
        #             return False

        #         return True
