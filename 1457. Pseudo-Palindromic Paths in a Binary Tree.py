# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict


class Solution:
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:

        # my second solution
        #

        ans = [0]

        def is_pseudo_palindrome(cur):
            have_odd = False
            for v in cur.values():
                if v % 2 == 1:
                    if have_odd:
                        return 0
                    have_odd = True
            return 1

        def dfs(node, cur):
            if not node:
                return
            cur[node.val] += 1
            if not node.left and not node.right:
                ans[0] += is_pseudo_palindrome(cur)
            else:
                dfs(node.left, cur)
                dfs(node.right, cur)
            cur[node.val] -= 1
            if not cur[node.val]:
                del cur[node.val]

        dfs(root, defaultdict(int))

        return ans[0]

        # my first solution
        #
        # def is_pseudo_palindrome(arr):
        #     meet_odd = False
        #     for num in arr:
        #         if num % 2 == 1:
        #             if meet_odd:
        #                 return False
        #             meet_odd = True
        #     return True
        #
        # ans = 0
        #
        # nums = [0 for _ in range(9)]
        #
        # def dfs(node):
        #     nonlocal ans
        #     nums[node.val - 1] += 1
        #     if not node.left and not node.right:
        #         ans += is_pseudo_palindrome(nums)
        #     else:
        #         if node.left:
        #             dfs(node.left)
        #         if node.right:
        #             dfs(node.right)
        #     nums[node.val - 1] -= 1
        #
        # dfs(root)
        #
        # return ans

        # official solution
        #
        # count = 0
        #
        # stack = [(root, 0)]
        # while stack:
        #     node, path = stack.pop()
        #     if node is not None:
        #         # compute occurences of each digit
        #         # in the corresponding register
        #         path = path ^ (1 << node.val)
        #         # if it's a leaf, check if the path is pseudo-palindromic
        #         if node.left is None and node.right is None:
        #             # check if at most one digit has an odd frequency
        #             if path & (path - 1) == 0:
        #                 count += 1
        #         else:
        #             stack.append((node.right, path))
        #             stack.append((node.left, path))
        #
        # return count