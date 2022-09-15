# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:

        def is_pseudo_palindrome(arr):
            meet_odd = False
            for num in arr:
                if num % 2 == 1:
                    if meet_odd:
                        return False
                    meet_odd = True
            return True

        ans = 0

        nums = [0 for _ in range(9)]

        def dfs(node):
            nonlocal ans
            nums[node.val - 1] += 1
            if not node.left and not node.right:
                ans += is_pseudo_palindrome(nums)
            else:
                if node.left:
                    dfs(node.left)
                if node.right:
                    dfs(node.right)
            nums[node.val - 1] -= 1

        dfs(root)

        return ans