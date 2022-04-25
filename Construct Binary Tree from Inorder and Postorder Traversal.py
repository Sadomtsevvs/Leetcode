# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> Optional[TreeNode]:
        """ my first solution, not optimal
        if not inorder:
            return None
        for i in reversed(range(len(postorder))):
            if postorder[i] in inorder:
                node = TreeNode(postorder.pop(i))
                break
        in_index = inorder.index(node.val)
        node.left = self.buildTree(inorder[:in_index], postorder)
        node.right = self.buildTree(inorder[in_index + 1:], postorder)
        return node
        """

        # my second solution
        if not inorder:
            return None
        node = TreeNode(postorder.pop())
        in_index = inorder.index(node.val) # this line is not good
        node.right = self.buildTree(inorder[in_index + 1:], postorder)
        node.left = self.buildTree(inorder[:in_index], postorder)
        return node

        """ optimal solution from leetcode
        indexed_inorder = {val: i for i, val in enumerate(inorder)}

        def build_rec(start, end):
            if start > end:
                return None
            root = TreeNode(postorder.pop())
            mid = indexed_inorder[root.val]
            root.right = build_rec(mid + 1, end)
            root.left = build_rec(start, mid - 1)
            return root

        return build_rec(0, len(inorder) - 1)
        """
