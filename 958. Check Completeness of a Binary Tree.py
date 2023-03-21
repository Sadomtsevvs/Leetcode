# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:

        nodes = [root]
        find_empty = False
        while nodes:
            next_nodes = []
            for node in nodes:
                if not node:
                    find_empty = True
                    continue
                if find_empty:
                    return False
                next_nodes.append(node.left)
                next_nodes.append(node.right)
            nodes = next_nodes

        return True
