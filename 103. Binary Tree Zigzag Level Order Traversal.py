# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        result = []
        nodes_to_traverse = [root]
        left_first = True
        while nodes_to_traverse:
            sub_result = []
            next_nodes = []
            while nodes_to_traverse:
                node = nodes_to_traverse.pop()
                sub_result.append(node.val)
                if left_first:
                    if node.left is not None:
                        next_nodes.append(node.left)
                    if node.right is not None:
                        next_nodes.append(node.right)
                else:
                    if node.right is not None:
                        next_nodes.append(node.right)
                    if node.left is not None:
                        next_nodes.append(node.left)
            left_first = not left_first
            result.append(sub_result)
            nodes_to_traverse[:] = next_nodes[:]
        return result
