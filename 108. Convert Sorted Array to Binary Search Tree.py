# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: list[int]):
        if len(nums) == 0:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])
        mid = len(nums)//2
        return TreeNode(nums[mid],
                        self.sortedArrayToBST(nums[:mid]),
                        self.sortedArrayToBST(nums[mid+1:]))


_nums = [-10,-4,-3,0,5,9,11]
# Input: nums = [-10,-3,0,5,9]
# Output: [0,-3,9,-10,null,5]
# Explanation: [0,-10,5,null,-3,null,9] is also accepted:
res = Solution().sortedArrayToBST(_nums)
pass
