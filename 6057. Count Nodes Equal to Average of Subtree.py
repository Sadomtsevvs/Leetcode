from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:

        ans = [0]

        def traverse(node):
            if not node:
                return 0, 0

            val = node.val
            left_sum, left_num = traverse(node.left)
            right_sum, right_num = traverse(node.right)

            if (val + left_sum + right_sum) // (1 + left_num + right_num) == val:
                ans[0] += 1

            return val + left_sum + right_sum, 1 + left_num + right_num

        traverse(root)
        return ans[0]
