# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:

        def longest_path(root: TreeNode) -> List[int]:
            nonlocal maxval

            if not root:
                return [0, 0]

            inr = dcr = 1
            if root.left:
                left = longest_path(root.left)
                if (root.val == root.left.val + 1):
                    dcr = left[1] + 1
                elif (root.val == root.left.val - 1):
                    inr = left[0] + 1

            if root.right:
                right = longest_path(root.right)
                if (root.val == root.right.val + 1):
                    dcr = max(dcr, right[1] + 1)
                elif (root.val == root.right.val - 1):
                    inr = max(inr, right[0] + 1)

            maxval = max(maxval, dcr + inr - 1)
            return [inr, dcr]

        maxval = 0
        longest_path(root)
        return maxval


        # doesn't work
        #
        # ans = [0]
        #
        # def helper(root):
        #     if not root:
        #         return -float('inf'), 0
        #     left_val, right_val = -float('inf'), -float('inf')
        #     left_direct, right_direct = 0, 0
        #     if root.left:
        #         left_val, left_direct = helper(root.left)
        #     if root.right:
        #         right_val, right_direct = helper(root.right)
        #     if abs(root.val - left_val) == 1 and abs(root.val - right_val) == 1:
        #         ans[0] = max(ans[0], left_direct + right_direct + 1)
        #     if abs(root.val - left_val) == 1:
        #         left_direct += 1
        #     if abs(root.val - right_val) == 1:
        #         right_direct += 1
        #     if not abs(root.val - left_val) == 1 and not abs(root.val - right_val) == 1:
        #         left_direct, right_direct = 0, 0
        #     return root.val, max(left_direct, right_direct, 1)
        #
        # num, res = helper(root)
        #
        # return max(ans[0], res)


_root = TreeNode(2, TreeNode(1), TreeNode(3))
_root = TreeNode(3, TreeNode(4, None, TreeNode(2, None, TreeNode(1))))
print(Solution().longestConsecutive(_root))
