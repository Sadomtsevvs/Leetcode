# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def isEqual(node1, node2):
            if node1 is None and node2 is None:
                return True
            if node1 is None or node2 is None:
                return False
            return node1.val == node2.val and isEqual(node1.left, node2.left) and isEqual(node1.right, node2.right)

        if isEqual(root, subRoot):
            return True

        if not root or not subRoot:
            return False

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

        """ my first solution, without one recursion
        def isEqual(node1, node2):
            if node1 is None and node2 is None:
                return True
            if node1 is None or node2 is None:
                return False
            return node1.val == node2.val and isEqual(node1.left, node2.left) and isEqual(node1.right, node2.right)

        nodes_to_check = [root]
        while nodes_to_check:
            node = nodes_to_check.pop()
            if isEqual(node, subRoot):
                return True
            if node.left:
                nodes_to_check.append(node.left)
            if node.right:
                nodes_to_check.append(node.right)

        return False
        """