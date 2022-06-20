from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:

        result = [0]

        def depth(node):
            if not node:
                return float('inf')
            val = min(depth(node.left), depth(node.right))
            node.val = 0 if val == float('inf') else 1 + val
            if node.val % 3 == 1:
                result[0] += 1
            return node.val

        depth(root)

        if root.val % 3 == 0:
            if not root.left and not root.right:
                result[0] += 1
            # elif not root.left or (root.left and root.left.val % 3 != 1) and not root.right or (root.right and root.right.val % 3 != 1):
            elif not root.left or (root.left.val % 3 != 1) and not root.right or (root.right.val % 3 != 1):
                result[0] += 1

        return result[0]


_root = TreeNode(0, TreeNode(0, TreeNode(0), TreeNode(0)))
_root = TreeNode(0, TreeNode(0, TreeNode(0, TreeNode(0, TreeNode(0, TreeNode(0, TreeNode(0)))))))
_root = TreeNode(0, TreeNode(0, TreeNode(0, TreeNode(0))), TreeNode(0, TreeNode(0, TreeNode(0, TreeNode(0, TreeNode(0))))))
# _root = TreeNode(0)
# _root = TreeNode(0, None, TreeNode(0))
print(Solution().minCameraCover(_root))
