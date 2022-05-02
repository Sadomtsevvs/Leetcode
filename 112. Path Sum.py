# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        """ recursive solution
        if not root:
            return False

        def backtrack(cur_sum, cur_node):
            if not cur_node.left and not cur_node.right and cur_sum + cur_node.val == targetSum:
                return True
            if cur_node.left:
                if backtrack(cur_sum + cur_node.val, cur_node.left):
                    return True
            if cur_node.right:
                if backtrack(cur_sum + cur_node.val, cur_node.right):
                    return True
            return False

        return backtrack(0, root)
        """

        if not root:
            return False

        stack = [(root, 0)]

        while stack:
            cur_node, cur_sum = stack.pop()
            if not cur_node.left and not cur_node.right:
                if cur_sum + cur_node.val == targetSum:
                    return True
                continue
            if cur_node.left:
                stack.append((cur_node.left, cur_sum + cur_node.val))
            if cur_node.right:
                stack.append((cur_node.right, cur_sum + cur_node.val))
        return False
