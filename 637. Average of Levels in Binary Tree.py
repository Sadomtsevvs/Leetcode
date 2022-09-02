# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        result = []
        layer = [root]
        while layer:
            next_layer = []
            sm = 0
            for node in layer:
                sm += node.val
                if node.left:
                    next_layer.append(node.left)
                if node.right:
                    next_layer.append(node.right)
            result.append(sm / len(layer))
            layer = next_layer
        return result