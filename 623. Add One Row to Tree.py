# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val, root)
        parents = [root]
        for i in range(2, depth):
            parents = [node for parent in parents for node in (parent.left, parent.right) if node]
        for parent in parents:
            parent.left = TreeNode(val, parent.left)
            parent.right = TreeNode(val, None, parent.right)
        return root


# Example 1:
# Input: root = [4,2,6,3,1,5], val = 1, depth = 2
# Output: [4,1,1,2,null,null,6,3,1,5]
#
# Example 2:
# Input: root = [4,2,null,3,1], val = 1, depth = 3
# Output: [4,2,null,1,1,3,null,null,1]
