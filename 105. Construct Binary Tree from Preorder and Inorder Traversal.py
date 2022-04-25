# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
        """
        if not inorder:
            return None
        node = TreeNode(preorder[0])
        in_index = inorder.index(node.val) # this line is not good
        node.left = self.buildTree(inorder[:in_index], preorder[1:])
        node.right = self.buildTree(inorder[in_index + 1:], preorder[1:])
        return node
        """

        reversed_preorder = preorder[::-1]
        indexed_inorder = {val: i for i, val in enumerate(inorder)}

        def build_rec(start, end):
            if start > end:
                return None
            node = TreeNode(reversed_preorder.pop())
            mid = indexed_inorder[node.val]
            node.left = build_rec(start, mid - 1)
            node.right = build_rec(mid + 1, end)
            return node

        return build_rec(0, len(inorder) - 1)

