# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        result = []
        nodes_to_traverse = [root]
        result.append(root.val)
        while nodes_to_traverse:
            next_nodes = []
            for node in nodes_to_traverse:
                if node.left is not None:
                    next_nodes.append(node.left)
                if node.right is not None:
                    next_nodes.append(node.right)
            if next_nodes:
                result.append(next_nodes[-1].val)
            nodes_to_traverse[:] = next_nodes[:]
        return result
