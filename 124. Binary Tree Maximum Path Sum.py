# Definition for a binary tree node.
from functools import cache


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    @cache
    def best_node_sum(self, root) -> int:
        if not root:
            return 0
        return max(root.val, root.val + max(self.best_node_sum(root.left), self.best_node_sum(root.right)))

    def maxPathSum(self, root) -> int:
        if not root:
            return -float('inf')
        bns_left = self.best_node_sum(root.left)
        bns_right = self.best_node_sum(root.right)
        return max(self.maxPathSum(root.left),
                   self.maxPathSum(root.right),
                   root.val,
                   root.val + bns_left,
                   root.val + bns_right,
                   root.val + bns_left + bns_right)

    # solution from LC
    #
    # def maxend(node):
    #     if not node:
    #         return 0
    #     left = maxend(node.left)
    #     right = maxend(node.right)
    #     self.max = max(self.max, left + node.val + right)
    #     return max(node.val + max(left, right), 0)
    #
    # self.max = -float('inf')
    # maxend(root)
    # return self.max


_root = TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
_root = TreeNode(-3)
# Input: root = [-10,9,20,null,null,15,7]
# Output: 42
# Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.

print(Solution().maxPathSum(_root))
