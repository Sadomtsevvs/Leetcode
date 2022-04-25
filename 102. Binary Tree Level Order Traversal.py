# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        result = []
        nodes_to_traverse = [root]
        while nodes_to_traverse:
            sub_result = []
            next_nodes = []
            for node in nodes_to_traverse:
                sub_result.append(node.val)
                if node.left is not None:
                    next_nodes.append(node.left)
                if node.right is not None:
                    next_nodes.append(node.right)
            result.append(sub_result)
            nodes_to_traverse[:] = next_nodes[:]
        return result
