# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        ans = 0

        nodes = [(root, 0)]

        while nodes:
            next_nodes = []
            first, last = -1, -2
            for node, idx in nodes:
                if first == -1:
                    first = idx
                last = idx
                if node.left:
                    next_nodes.append((node.left, 2 * idx))
                if node.right:
                    next_nodes.append((node.right, 2 * idx + 1))
            ans = max(ans, last - first + 1)
            nodes = next_nodes

        return ans


# Example 1:
# Input: root = [1,3,2,5,3,null,9]
# Output: 4
# Explanation: The maximum width exists in the third level with length 4 (5,3,null,9).
#
# Example 2:
# Input: root = [1,3,2,5,null,null,9,6,null,7]
# Output: 7
# Explanation: The maximum width exists in the fourth level with length 7 (6,null,null,null,null,null,7).
#
# Example 3:
# Input: root = [1,3,2,5]
# Output: 2
# Explanation: The maximum width exists in the second level with length 2 (3,2).