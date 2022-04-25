# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root, maxval=float('inf'), minval=-float('inf')) -> bool:
        if not root:
            return True
        if not (maxval > root.val > minval):
            return False
        if not root.right and not root.left:
            return True
        if not root.left and root.right is not None:
            return self.isValidBST(root.right, maxval, root.val)
        elif not root.right and root.left is not None:
            return self.isValidBST(root.left, root.val, minval)
        return self.isValidBST(root.right, maxval, root.val) and self.isValidBST(root.left, root.val, minval)

        # official stack solution
        #
        # if not root:
        #     return True
        # stack = [(root, -math.inf, math.inf)]
        # while stack:
        #     root, lower, upper = stack.pop()
        #     if not root:
        #         continue
        #     val = root.val
        #     if val <= lower or val >= upper:
        #         return False
        #     stack.append((root.right, val, upper))
        #     stack.append((root.left, lower, val))
        # return True


_root = TreeNode(5, None, TreeNode(8, TreeNode(6, None, TreeNode(7)), TreeNode(10)))
# _root = TreeNode(5, TreeNode(4), TreeNode(6))
print(Solution().isValidBST(_root))
