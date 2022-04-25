# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if not root:
            return result
        roots_to_traverse = [root]
        while roots_to_traverse:
            root_to_traverse = roots_to_traverse[-1]
            if root_to_traverse.right is None and root_to_traverse.left is None:
                result.append(roots_to_traverse.pop().val)
                continue
            if root_to_traverse.right is not None:
                roots_to_traverse.append(root_to_traverse.right)
                root_to_traverse.right = None
            if root_to_traverse.left is not None:
                roots_to_traverse.append(root_to_traverse.left)
                root_to_traverse.left = None
        return result
