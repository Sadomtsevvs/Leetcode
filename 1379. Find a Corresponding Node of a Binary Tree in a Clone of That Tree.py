# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        stack = [(original, cloned)]
        while stack:
            node, c_node = stack.pop()
            if node is None:
                continue
            if node == target:
                return c_node
            stack.append((node.left, c_node.left))
            stack.append((node.right, c_node.right))
        return None
